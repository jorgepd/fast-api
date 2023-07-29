# imports
from fastapi import APIRouter, status

# custom imports
from config import logger
from src.db import simple

def get_service(id):
    return simple.select(id)

def post_service(message):
    simple.insert(message)

def put_service():
    return 'Call completed'

def delete_service(id):
    simple.delete(id)


