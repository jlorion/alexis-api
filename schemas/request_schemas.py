from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from decimal import Decimal
from datetime import date
from uuid import UUID

class ClientSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    contact: Optional[str] = None
    email: Optional[EmailStr] = None

class ServiceSchema(BaseModel):
    name: Optional[str] = None
    rate: Optional[Decimal] = None

class BookingSchema(BaseModel):
    client_id: UUID 
    booking_date: date  

class UpdateBookingSchema(BaseModel):
    booking_date: Optional[date] = None

class ServiceListSchema(BaseModel):
    service_id: UUID
    hours_rendered: Decimal

class CostSchema(BaseModel):
    service_id: UUID
    hours_rendered: Decimal
    cost: Decimal

class TransactionSchema(BaseModel):
    booking_id: UUID
    payment: Decimal = Field(default=0, max_digits=10, decimal_places=3) 