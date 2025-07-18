from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, Relationship
from pydantic import EmailStr
from uuid import uuid4, UUID
from typing import Optional
from decimal import Decimal
from datetime import date


class Clients(SQLModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), unique=True, primary_key=True)
    first_name: str
    last_name: str
    address: str
    contact: str
    email: EmailStr = Field(unique=True, index=True, max_length=255)

class Services(SQLModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), unique=True, primary_key=True)
    name: str
    rate: Decimal = Field(default=0, max_digits=10, decimal_places=3)

    

class Booking(SQLModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), unique=True, primary_key=True)
    booking_date: date = Field(unique=True)
    client_id: UUID
    

class Services_list(SQLModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), unique=True, primary_key=True)
    booking_id: UUID
    services_id:  UUID
    hours_rendered: Decimal
    service_cost: Decimal= Field(default=0, max_digits=10, decimal_places=3, nullable=True)

class Inventory(SQLModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), unique=True, primary_key=True)
    service_id: UUID
    name: str  
    quantity: int

class Transaction(SQLModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), unique=True, primary_key=True)
    booking_id: UUID
    transaction_date: date
    payment: Decimal = Field(default=0, max_digits=10, decimal_places=3) 
    change: Decimal = Field(default=0, max_digits=10, decimal_places=3)
    total: Decimal = Field(default=0, max_digits=10, decimal_places=3)