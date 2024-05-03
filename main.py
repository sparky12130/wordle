from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def sayHello():
    return {"message": "Hello"}

@app.get("/")
def sayWelcome():
    return{"message":"Welcome"}