from fastapi import FastAPI  #

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ultimo teste de todos!!!!!!!"}


@app.get("/v1")
async def root_v1():
    return {"message": "OLá ola v33333333 no v1"}


@app.get("/v2")
async def root_v2():
    return {"message": "OLá ola v2"}


@app.get("/v3")
async def root_v3():
    return {"message": "Acabei de ser atualizado"}


@app.get("/v4")
async def root_v4():
    return {"message": "OLá ola v4"}
