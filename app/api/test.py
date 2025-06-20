#test.py
# to test whether the app is running or not.

from fastapi import FastAPI, APIRouter

router = APIRouter(tags=["test"])

@router.get("/", tags=["test"])
async def test_point():
    return "test success"