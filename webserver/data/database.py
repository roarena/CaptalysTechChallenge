from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from webserver.config import DATABASE_URI

engine = create_engine(DATABASE_URI)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()