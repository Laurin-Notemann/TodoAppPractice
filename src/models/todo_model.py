from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import Date
from dataclasses import dataclass
from datetime import datetime

Base = declarative_base()


@dataclass
class Todo(Base):
    __tablename__ = "Todo"

    id: uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    todo_entry: str = Column(String)

    date: datetime = Column(Date)
