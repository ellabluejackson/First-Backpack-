# notes endpoints go here

from fastapi import APIRouter

router = APIRouter(prefix="/notes", tags=["notes"])

# add get all, get one, create, delete
