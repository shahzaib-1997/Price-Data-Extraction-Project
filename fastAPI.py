import json
import asyncio
import uvicorn
from fastapi import FastAPI, HTTPException, status
from selenium import webdriver
from pydantic import BaseModel
from dollar_set_fx import login, main


def run_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


# Global variables
scraper_running = False

app = FastAPI()


class Credentials(BaseModel):
    username: str
    password: str


@app.get("/get_data")
async def get_data():
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


@app.post("/initiate-scraper/")
async def initiate_scraper(credentials: Credentials):
    global scraper_running
    try:
        if scraper_running:
            return {"message": "Scraper is already running."}

        driver = run_driver()
        check = login(credentials.username, credentials.password, driver)
        if check:
            asyncio.create_task(main(driver))
            scraper_running = True
            return {"message": "Scraper Initiated."}
        raise HTTPException(status_code=401, detail="Unable to login!")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
