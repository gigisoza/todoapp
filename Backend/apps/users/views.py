from fastapi import APIRouter, HTTPException
from beanie import PydanticObjectId
from typing import List
from Backend.apps.users.documents import Backend
router = APIRouter(prefix="")


@router.get("/get/item", response_model=List[Backend])
async def register_user():
    return await Backend.find_all().to_list()


@router.post("/add/item", status_code=201, response_model=Backend)
async def register_user(item: Backend):
    return await item.save()


@router.post("/update/item/{item_id}", status_code=200, response_model=Backend)
async def register_user(item_id: str, item: Backend):
    if todo := await Backend.find_one(Backend.id == PydanticObjectId(item_id)):
        todo.item = item.item
        if item.description:
            todo.desc = item.description
        return await todo.save()
    raise HTTPException(status_code=400, detail="not found")


@router.post("/delete/item", response_model=Backend)
async def delete_item(item_id: str, item: Backend):
    if todo := await Backend.find_one(Backend.id == PydanticObjectId(item_id)):
        return await Backend.delete(todo)
    raise HTTPException(status_code=400, detail="not found")
