from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
def on_startup():
    print('Hi')
    # create_db_and_tables()

@app.get("/")
async def read_root():
    return {"hello World"}