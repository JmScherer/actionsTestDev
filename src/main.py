""" This is the entrypoint to our test application """

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """ This is our root function for FastAPI test application """
    return {"message": "Hello World"}
