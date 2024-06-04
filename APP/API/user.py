from fastapi  import APIRouter

router = APIRouter()

@router.get("/user")
async def read_items():
    return [{"user_name": "pierre", "user_name": "paul"}]
