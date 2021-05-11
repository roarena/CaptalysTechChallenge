from fastapi import FastAPI
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists


from webserver.data import ReposRequests
from webserver.data.database import Base
from webserver.data.models.models import User, Repositories
from webserver.config import DATABASE_URI


app = FastAPI()
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

@app.get("/repositories/")
async def read_item(username: str, from_local: Optional[bool]=False):
    return ReposRequests.get_repos(username, from_local)


@app.get("/repositories/{repo}")
async def read_item(repo, username: str, save_data: bool = False):
    return ReposRequests.get_repo_details(username, repo, save_data)

#FOR DEBUG PURPOSE
@app.get("/recreate_db")
async def read_item():
        if(database_exists(engine.url)):
            Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        return "DB Reloaded"
