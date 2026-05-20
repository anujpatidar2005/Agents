from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Anuj"}
@app.post("/data")
def submit():
    return {"message": "Data Submitted"}