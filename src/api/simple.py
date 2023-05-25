# imports
from fastapi import APIRouter, status

# custom imports
from config import logger
from src.services import simple

router = APIRouter(prefix='/simple', tags=['Simple'])

@router.get('/', status_code=status.HTTP_200_OK)
def get():
    '''
    GET endpoint
    '''
    return simple.get_service()
