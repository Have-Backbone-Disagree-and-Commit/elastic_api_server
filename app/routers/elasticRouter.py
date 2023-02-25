from fastapi import APIRouter
router = APIRouter()
import elasticsearch
import os

from dotenv import load_dotenv
load_dotenv()
CLOUD_ID = os.getenv("CLOUD_ID")
CLOUD_USER = os.getenv("CLOUD_USER")
CLOUD_PSWD = os.getenv("CLOUD_PSWD")

es = elasticsearch.Elasticsearch(
    cloud_id=CLOUD_ID,
    http_auth=(CLOUD_USER, CLOUD_PSWD),
)


@router.post("/send_data", tags=["slack"])
async def send_data(data : dict):
    try:
        for key, value in data.items():
            res = es.index(index="crawl_database", body=value)
            print(res)
        return res
    except Exception as e:
        return 

@router.get("/get_test/{id}", tags=["slack"])
async def get_test(id: int):
    return id

