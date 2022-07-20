from sqlalchemy import Column, Integer, String
from databases.sqlite_db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True) 
    name = Column(String) 
    email = Column(String, default=True)
    phone = Column(String, default=True)
