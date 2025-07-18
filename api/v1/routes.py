from fastapi import APIRouter
from api.v1.endpoints import client, services, booking

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(client.clients_routes)
v1_router.include_router(services.service_router)
v1_router.include_router(booking.booking_router)