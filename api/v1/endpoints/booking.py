
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
from schemas.request_schemas import BookingSchema, UpdateBookingSchema, ServiceListSchema, CostSchema

booking_router=  APIRouter(prefix='/booking', tags=['BOOKING'])
dbSession = Annotated[AsyncSession, Depends(getDatabaseSesssion)]



@booking_router.post("/")
async def new_booking(db: dbSession, booking_data: BookingSchema, services: list[ServiceListSchema]):
    try:
        booking= Booking(**booking_data.dict())
        chosen_services_stmnt = select(Services).where(Services.id.in_([service.service_id for service in services]))
        chosen_rslt = await db.exec(chosen_services_stmnt)
        serv_list = chosen_rslt.fetchall()
        print(serv_list)
        my_dict = {}
        for serv in serv_list:
            print(serv[0].rate)
            my_dict[str(serv[0].id)] = serv[0].rate
        print(my_dict)
        service_list = [Services_list(
                booking_id= booking.id, 
                services_id= service.service_id,
                service_cost= my_dict[str(service.service_id)] * service.hours_rendered,
                hours_rendered= service.hours_rendered
        ) for service in services]
        print(service_list)
        db.add(booking)
        db.add_all(service_list)
        await db.commit()
        return {"status": "success", "booking": "booking successfully added"}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))

@booking_router.patch("/{booking_id}")
async def update_booking(db:dbSession, booking_id: UUID, new_data: UpdateBookingSchema):
    try:
        booking_stmnt = select(Booking).where(Booking.id == booking_id)
        booking_rslt= await db.exec(booking_stmnt)
        booking = booking_rslt.one_or_none()
        print(booking)
        if booking is None: 
            raise HTTPException(status_code=400, detail="booking does not exist ")
        update_data = new_data.model_dump(exclude_unset=True)
        booking.booking_date = new_data.booking_date
        db.add(booking)
        await db.commit()
        return {"status": "succces", "message": "successfully updated booking "}
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail=str(err))



