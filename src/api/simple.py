# imports
from fastapi import APIRouter, status, HTTPException
import json

# custom imports
from config import logger
from src.services import simple
from . import models


router = APIRouter(prefix='/simple', tags=['Simple'])


@router.get('/', status_code=status.HTTP_200_OK)
def get(id=None):
    '''
    GET endpoint
    '''
    logger.info('get()')
    df = simple.get_service(id)
    return json.loads(df.to_json(orient='records'))


@router.post('/', status_code=status.HTTP_201_CREATED)
def post(message: models.MessageRequest):
    '''
    POST endpoint
    '''
    logger.info('post()')
    return simple.post_service(message)


@router.put('/', status_code=status.HTTP_200_OK)
def put():
    '''
    PUT endpoint
    '''
    logger.info('put()')
    # status.HTTP_404_NOT_FOUND
    return simple.put_service()


@router.delete('/', status_code=status.HTTP_200_OK)
def delete(id=None):
    '''
    DELETE endpoint
    '''
    logger.info('delete()')
    if not simple.delete_service(id):
        raise HTTPException(status_code=404, detail="Item not found")
