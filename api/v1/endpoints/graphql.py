from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, UploadFile, Form, File, Request
from sqlmodel import Session, select, Field
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Annotated, List, Dict
from uuid import UUID, uuid4
import strawberry
from strawberry.fastapi import GraphQLRouter
from database.models import Clients
from database.database import getDatabaseSesssion


dbSession = Annotated[AsyncSession, Depends(getDatabaseSesssion)]

async def get_dependencies(request: Request, db: dbSession):
    return {
        "request": request, 
        "session": db
    }

@strawberry.type
class ClientsType:
    id: UUID     
    first_name: str
    last_name: str
    address: str
    contact: str
    email: str 

@strawberry.type
class Query:
    @strawberry.field
    async def get_all_clients(self, info) -> List[ClientsType]:
        db: AsyncSession = info.context["session"]
        rslt = await db.exec(select(Clients))
        clients = rslt.all()
        return [ClientsType(**client.dict()) for client in clients]

    @strawberry.field
    async def get_client(self, info, id: UUID) -> ClientsType:
        db: AsyncSession = info.context["session"]
        rslt = await db.exec(select(Clients).where(Clients.id == id))
        client = rslt.all()
        return ClientsType(**client.dict())

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema, context_getter=get_dependencies)