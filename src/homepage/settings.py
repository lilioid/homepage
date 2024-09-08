import sys
from typing import Annotated, List, Self

from colorama import Fore, Style
from fastapi import Depends, Request
from pydantic import Field
from pydantic_core import ValidationError
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEV_MODE: bool = Field(default=False, description="Whether develpoment-only features should be enabled")
    BIND: List[str] = Field(default=["127.0.0.1:8000"], description="On which socket address the webserver should bind")

    @classmethod
    def from_env(cls) -> Self:
        return cls(_env_file=".env.local")

    @classmethod
    def from_argv(cls) -> Self:
        try:
            return cls(_cli_parse_args=True, _cli_prog_name="homepage", _env_file=".env.local")
        except ValidationError as e:
            print(f"{Fore.RED}Could not start homepage server due to configuration errors{Fore.RESET}")
            print(
                f"{Fore.RED}To supply these values, either set them via command-line arguments "
                + "(call homepage --help for details) or environment variables{Fore.RESET}"
            )
            for i in e.errors():
                print(
                    f"  {Fore.RED}{Style.DIM}-{Style.NORMAL} {'.'.join(i['loc'])}"
                    + f"{Style.DIM}:{Style.NORMAL} {i['msg']}{Fore.RESET}"
                )

            sys.exit(1)

    @staticmethod
    def from_request(request: Request) -> Self:
        return request.app.state.settings


Settings = Annotated[Settings, Depends(Settings.from_request)]
