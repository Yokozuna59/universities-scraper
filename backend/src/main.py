from json import load

from fastapi import FastAPI

app = FastAPI()


@app.get("/templates")
async def templates():
    with open("../templates.json") as file:
        file_dict = load(file)
    return {"data": file_dict}


# @app.get("/templates/{major_traning_version}")
# async def plans_template(major: str, training: str, version: str):
#     with open(f"../template/{major}-{training}-{version}") as file:
#         file_dict = load(file)
#     return {"data": file_dict}


@app.get("/templates/cs-internship-new")
async def cs_internship_new():
    with open("../template/cs-internship-new.json") as file:
        file_dict = load(file)
    return {"data": file_dict}


@app.get("/templates/cs-summer-new")
async def cs_summer_new():
    with open("../template/cs-summer-new.json") as file:
        file_dict = load(file)
    return {"data": file_dict}


@app.get("/templates/cs-summer-old")
async def cs_summer_old():
    with open("../template/cs-summer-old.json") as file:
        file_dict = load(file)
    return {"data": file_dict}


@app.get("/templates/swe-summer-new")
async def swe_summer_new():
    with open("../template/swe-summer-new.json") as file:
        file_dict = load(file)
    return {"data": file_dict}


@app.get("/templates/swe-summer-old")
async def swe_summer_old():
    with open("../template/swe-summer-old.json") as file:
        file_dict = load(file)
    return {"data": file_dict}
