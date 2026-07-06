from sqlalchemy import Column, BigInteger, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.db.database import Base

class Url(Base):
    __tablename__ = "urls"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    original_url = Column(Text, nullable=False)

    short_code = Column(String(10), unique=True, nullable=False)

    click_count = Column(Integer, default=0, nullable=False)

    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)

    last_accessed_at = Column(DateTime(timezone=True),nullable=True)