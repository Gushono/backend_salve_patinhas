from fastapi import FastAPI  #

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "OLá mundasasa"}


@app.get("/v1")
async def root_v1():
    return {"message": "OLá ola v1"}


@app.get("/v2")
async def root_v2():
    return {"message": "OLá ola v2"}


@app.get("/v3")
async def root_v3():
    return {"message": "OLá ola v3"}
