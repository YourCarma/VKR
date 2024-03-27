from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from services.collecting.router import router as router_collecting
app = FastAPI(
    title="WARMONGER"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router_collecting
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)