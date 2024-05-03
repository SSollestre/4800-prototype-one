from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/user')
async def get_user():
    return {"user": "John"}