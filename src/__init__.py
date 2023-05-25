# imports
from fastapi import FastAPI

# custom imports
from config import settings, logger
from src.api import simple


def create_app():
    logger.info(f'Creating app with {settings.env} config...')
    app = FastAPI(title=settings.app_name)
    logger.info(f'App ready')
    return app

app = create_app()

app.include_router(simple.router)
