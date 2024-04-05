import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from utils import path

load_dotenv()


class Config(BaseSettings):
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    URL: str = os.getenv('URL')
    TIMEOUT: float = os.getenv('TIMEOUT')


config = Config(_env_file=path.relative_from_root(f'.env.{Config()}'))
