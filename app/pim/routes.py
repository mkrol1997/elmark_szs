from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/pim", tags=["pim"])


@router.get("/")
def get_hello_world():
    payload = {"response": "Hello world"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
