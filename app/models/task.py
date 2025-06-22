# task.py
from sqlalchemy import (Integer, String, Boolean, 
                        Column, DateTime, ForeignKey
                        )
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Task(Base):
    __tablename__ = "task"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_date = Column(DateTime)
    priority = Column(String(10), default="medium")
    is_completed = Column(Boolean, default=False)

    user = relationship("User", backref="task")