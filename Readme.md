# Price-Data-Extraction-Project

This project aims to extract price data from the website https://dolar.set-icap.com/ at regular intervals using provided username and password then save that data along with time stamp in a json file and make it accessible via an API.


# Requirements

Data extraction from https://dolar.set-icap.com/ every 30 seconds.
Access to scraped data via API.
Authentication using provided username and password.


# Setup

First install python from its official website.

https://www.python.org/downloads/


Then, Clone the repository:

git clone https://github.com/shahzaib-1997/Price-Data-Extraction-Project.git

Open the terminal in project directory and Install dependencies using:

pip install -r requirements.txt

Configure your username and password in config.py.


# Usage

Run the data extraction script:

python dollar_set_fx.py

This script will extract data from the website every 30 seconds and save it in data.json file.

Run the server to access data:

uvicorn fastAPI:app --reload 

Access the scraped data via API:

Endpoint: localhost:8000/
Method: GET
Parameters: None


API Response Format

The API will respond with the extracted price data in JSON format e.g.:

{
    "time_stamp": "Fri Mar 22 00:39:06 2024", 
    "value": "3,904.95"
}
