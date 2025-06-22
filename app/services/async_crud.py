from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from fastapi import HTTPException, status

class AsyncCRUD:
    @staticmethod
    async def create(session: AsyncSession, model, data: dict):
        try:
            instance = model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance
        except IntegrityError as e:
            await session.rollback()
            raise HTTPException(status_code=400, detail="Integrity error: likely a duplicate entry")
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def get(session: AsyncSession, model, filters: dict):
        stmt = select(model).filter_by(**filters)
        result = await session.execute(stmt)
        instance = result.scalar_one_or_none()
        if not instance:
            raise HTTPException(status_code=404, detail="Item not found")
        return instance

    @staticmethod
    async def update(session: AsyncSession, model, filters: dict, update_data: dict):
        stmt = update(model).filter_by(**filters).values(**update_data).execution_options(synchronize_session="fetch")
        result = await session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="No record updated")
        await session.commit()
        return {"status": "updated"}

    @staticmethod
    async def delete(session: AsyncSession, model, filters: dict):
        stmt = delete(model).filter_by(**filters).execution_options(synchronize_session="fetch")
        result = await session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="No record deleted")
        await session.commit()
        return {"status": "deleted"}

    @staticmethod
    async def list(session: AsyncSession, model, filters: dict = None):
        stmt = select(model)
        if filters:
            stmt = stmt.filter_by(**filters)
        result = await session.execute(stmt)
        return result.scalars().all()
