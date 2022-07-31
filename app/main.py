from fastapi import FastAPI  #

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "OLá mundasasa"}


@app.get("/v1")
async def root_v1():
    return {"message": "OLá ola v1"}
