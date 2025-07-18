
from sqlmodel.ext.asyncio.session import AsyncSession
from database.database import getDatabaseSesssion 
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import Annotated, List 
from uuid import UUID
import strawberry
from decimal import Decimal
from database.models import Booking, Services_list, Services
from datetime import date
from sqlalchemy.sql import select
from schemas.request_schemas import BookingSchema, UpdateBookingSchema, ServiceListSchema, CostSchema, TransactionSchema

booking_router=  APIRouter(prefix='/transaction', tags=['TRANSACTION'])
dbSession = Annotated[AsyncSession, Depends(getDatabaseSesssion)]

@booking_router.post("/")
async def new_booking(db: dbSession, transaction_data: TransactionSchema):
    try:
        booking_stmnt = select(Booking).where(Booking.id == transaction_data.booking_id)
        booking_rslt = await db.exe(booking_stmnt)
        
        return {"status": "success", "booking": "booking successfully added"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))




