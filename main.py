from fastapi import FastAPI
import uvicorn
from api.v1.routes import v1_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.include_router(v1_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.get('/')
async def welcome():
    return {'message': 'hello this is alexis-api'}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
