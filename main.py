from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from all origins (change '*' to a list of allowed origins if desired)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/user')
async def get_user():
    return {"user": "John"}
