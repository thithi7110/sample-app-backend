import requests,json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def Hello():
    return {"message":"Hello"}


@app.get("/zipcode")
async def ZipCode(zipcode:int = 0):
    url = f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
    r = requests.get(url)
    print(r.text)
    return json.loads(r.text)