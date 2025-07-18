from sqlmodel.ext.asyncio.session import AsyncSession
from database.database import getDatabaseSesssion 
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import Annotated, List 
from uuid import UUID
import strawberry
from database.models import Clients
from sqlmodel import select
from schemas.request_schemas import ClientSchema



clients_routes=  APIRouter(prefix='/clients', tags=['CLIENTS'])
dbSession = Annotated[AsyncSession, Depends(getDatabaseSesssion)]

@clients_routes.post("/")
async def new_client(db: dbSession, client_data: ClientSchema):
    try:
        client = Clients(**client_data.dict())
        db.add(client)
        await db.commit()
        return {"status": "success", "partner": "client successfully added"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@clients_routes.patch("/{client_id}")
async def update_client(db:dbSession, client_id: UUID, update_data: ClientSchema):
    client_stmnt = select(Clients).where(Clients.id == client_id)
    client_rslt = await db.exec(client_stmnt)
    client = client_rslt.one_or_none()
    if client is None: 
        raise HTTPException(status_code=400, detail="partner does not exist ")
    data = update_data.model_dump(exclude_unset=True)
    client.sqlmodel_update(data)
    db.add(client)
    await db.commit()
    return {"status": "succces", "message": "successfully updated client"}

