from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.types import PickleType
from sqlalchemy.orm import relationship

from webserver.data.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)

    repo = relationship("Repositories")


class Repositories(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_name = Column(String(255))
    url = Column(String(255))
    name = Column(String(255))
    is_private = Column(String(50))
    created_at = Column(String(50))
    updated_at = Column(String(50))
    size = Column(Integer)
    stargazers_count = Column(Integer)
    watchers_count = Column(Integer)