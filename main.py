from fastapi import FastAPI

app = FastAPI(title="Notes API")

@app.get("/")
def root():
    return {"message": "Notes API is running"}

@app.get("/notes")
def get_notes():
    return [
        {"id": 1, "title": "First note"},
        {"id": 2, "title": "Second note"}
    ]
