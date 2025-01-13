import logging
from datetime import datetime
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, Request
from sqlmodel import Field, Session, SQLModel, create_engine

from homepage.config import AppConfig

logger = logging.getLogger(__name__)


class WebmentionSentEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    src_uri: str
    target_uri: str
    date: datetime


def init(app: FastAPI, config: AppConfig):
    # connect to database file
    sqlite_url = f"sqlite:///{config.db_path}"
    connect_args = {"check_same_thread": False}
    logger.info("Connecting to database %s", sqlite_url)
    engine = create_engine(sqlite_url, connect_args=connect_args)

    # create all necessary tables
    logger.info("Ensuring database tables exist")
    SQLModel.metadata.create_all(engine)

    # store a reference to the engine in the app state
    app.state.sql_engine = engine


def get_session(request: Request) -> Session:
    engine = request.app.state.sql_engine
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
