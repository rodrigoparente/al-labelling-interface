# python imports
import os
from io import BytesIO

# third-party imports
from fastapi import APIRouter
from fastapi import Request
from fastapi import File
from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
import pandas as pd


active_router = APIRouter(tags=["active"])


@active_router.post("/upload_instances")
async def upload_instances(request: Request, file: UploadFile = File(...)):

    if not file.filename.endswith('.csv'):
        return {"error": "file extension must be .csv"}

    destination = os.path.join(os.getcwd(), 'app', 'backend', 'models')
    filename = os.path.join(destination, file.filename)

    if not os.path.exists(destination):
        os.makedirs(destination)

    try:
        df = pd.read_csv(BytesIO(file.file.read()))
    except Exception:
        return {"error": "There was an error reading the file"}

    instance = {
        "dataset_name": file.filename.replace('', '-').split('.')[0],
        "columns": list(df.columns),
        "entries": df.to_dict(orient='records')
    }

    new_instance = await request.app.mongodb["instances"].insert_one(jsonable_encoder(instance))
    instance = await request.app.mongodb["instances"].find_one({"_id": new_instance.inserted_id})

    try:
        contents = file.file.read()
        with open(filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"error": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"success": instance}
