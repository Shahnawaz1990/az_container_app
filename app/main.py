from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello" : "World1", "Uni" : "UIT University"}

@app.get("/about")
def index():
    return {"Institue Name" : "PIAIC"}