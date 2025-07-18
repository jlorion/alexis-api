from sqlmodel.ext.asyncio.session import AsyncSession
from database.database import getDatabaseSesssion 
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import Annotated, List 
from uuid import UUID
import strawberry
from database.models import Services
from sqlmodel import select
from schemas.request_schemas import ServiceSchema


service_router=  APIRouter(prefix='/services', tags=['SERVICES'])
dbSession = Annotated[AsyncSession, Depends(getDatabaseSesssion)]

@service_router.post("/")
async def new_service(db: dbSession, service_data: ServiceSchema):
    try:
        service= Services(**service_data.dict())
        db.add(service)
        await db.commit()
        return {"status": "success", "partner": "service successfully added"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@service_router.patch("/{service_id}")
async def update_service(db:dbSession, service_id: UUID, update_data: ServiceSchema):
    service_stmnt = select(Services).where(Services.id == service_id)
    service_rslt = await db.exec(service_stmnt)
    service = service_rslt.one_or_none()
    if service is None: 
        raise HTTPException(status_code=400, detail="service does not exist ")
    data = update_data.model_dump(exclude_unset=True)
    service.sqlmodel_update(data)
    db.add(service)
    await db.commit()
    return {"status": "succces", "message": "successfully updated service"}

@service_router.delete("/{service_id}")
async def delete_service(db:dbSession, service_id: UUID):
    # delete todo
    return {"status": "succces", "message": "successfully deleted  service"}

