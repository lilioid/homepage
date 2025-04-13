import logging
from datetime import datetime
from typing import Annotated, Optional

from fastapi import Depends, Request
from sqlalchemy import Engine
from sqlmodel import Field, Session, SQLModel, create_engine

logger = logging.getLogger(__name__)


class WebmentionSentEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    src_uri: str
    target_uri: str
    date: datetime


def connect_engine(db_path: str, debug: bool = False) -> Engine:
    uri = f"sqlite:///{db_path}"
    connect_args = {"check_same_thread": False}
    logger.info("Connecting to database %s", db_path)
    return create_engine(uri, connect_args=connect_args)


def init_state(engine: Engine):
    SQLModel.metadata.create_all(engine)


def get_session(request: Request) -> Session:
    engine = request.app.state.sql_engine
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
