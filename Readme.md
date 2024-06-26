# Price-Data-Extraction-Project

This project aims to extract price data from the website https://dolar.set-icap.com/ at regular intervals using username and password, provided via API request, then save that data along with time stamp in a json file and make it accessible via an API.


## Setup
First install python from its official website.

https://www.python.org/downloads/

Then, Clone the repository:

git clone https://github.com/shahzaib-1997/Price-Data-Extraction-Project.git

Open the terminal in project directory and Install dependencies using:

pip install -r requirements.txt

Configure your username and password in config.py.


## Usage
Run the server using command:

uvicorn fastAPI:app --reload 


## Initiate the scraper via API:
Endpoint: http://127.0.0.1:8000/initiate-scraper/
Method: POST
Parameters: username and password

### API Response Format
The API will respond with the extracted price data in JSON format e.g.:

#### On success
{
    "message": "Scraper Initiated."
    }

#### On login failure
{
    "detail": "Unable to login!"
    }

#### On server error
{
    "detail": "string"
    }


## Access the scraped data via API:
Endpoint: http://127.0.0.1:8000/get_data
Method: GET
Parameters: None

### API Response Format
The API will respond with the extracted price data in JSON format e.g.:

#### On success
{
    "time_stamp": "Fri Mar 22 00:39:06 2024", 
    "value": "3,904.95"
    }

#### On server error
{
    "detail": "string"
    }
## Test API:
Endpoint: http://127.0.0.1:8000/docs