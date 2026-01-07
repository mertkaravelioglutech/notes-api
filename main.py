from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/")
def root():
    return {"message": "Counter API is running"}

@app.get("/count")
def get_count():
    return {"count": counter}

@app.post("/increment")
def increment():
    global counter
    counter += 1
    return {"count": counter}
