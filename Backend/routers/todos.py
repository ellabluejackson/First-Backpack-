# todos endpoints go here

from fastapi import APIRouter

router = APIRouter(prefix="/todos", tags=["todos"])

# add get all, create, update, delete
