from typing import Annotated, Self

from fastapi import Depends, Request
from pydantic import BaseModel


class AppConfig(BaseModel):
    bind: str
    db_path: str
    dev_mode: bool

    @staticmethod
    def from_request(request: Request) -> Self:
        return request.app.extra["app_config"]


AppConfigDep = Annotated[AppConfig, Depends(AppConfig.from_request)]
