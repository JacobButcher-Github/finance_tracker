from fastapi import FastAPI

app = FastAPI()


@app.get("/check")
async def root():
    return {"message:": "Hello World"}
