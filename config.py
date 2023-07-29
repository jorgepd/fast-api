# imports
from pydantic import BaseSettings
import sqlalchemy
import logging
import yaml


class Settings(BaseSettings):
    env = 'DEV'
    app_name = 'fast-api Template'


def create_logger():
    conf_dict = yaml.load(open('logging.conf'), Loader=yaml.FullLoader)
    logging.config.dictConfig(conf_dict)
    return logging.getLogger()


settings = Settings()
logger = create_logger()
engine = sqlalchemy.create_engine('sqlite:///sqlite/database.db')
