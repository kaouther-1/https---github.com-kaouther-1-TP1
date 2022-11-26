from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
import os
load_dotenv()
# environement variables
API_Key = os.getenv("API_KEY")
EMAIL_ADDR = ""
PASSWORD = ""

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '99',
    'limit': '1',


}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'd53800e1-5c89-42d0-80ed-ebbf6e8fc2e7',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])

    print(json_string)
    print("hello")
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
