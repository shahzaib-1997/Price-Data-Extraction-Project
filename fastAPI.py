from fastapi import FastAPI, HTTPException, status
import json


app = FastAPI()


@app.get("/")
async def root():
    try:
        # Open the JSON file for reading
        with open("data.json", "r") as file:
            # Load JSON data from the file
            data = json.load(file)

        return data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"Error": str(e)},
        )
