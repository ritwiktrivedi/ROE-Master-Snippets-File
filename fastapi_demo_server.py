from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"message": "Tools in Data Science is for grownups."}


@app.get("/jecho")
async def jecho(query: str):
    data = {"query": query}
    return JSONResponse(content=data)


# add your own functions here

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run the server
# uvicorn fastapi_demo_server:app --reload
