import requests

def get_houses(price_range):
    API_KEY = "your_zillow_api_key"
    endpoint = "http://www.zillow.com/webservice/GetSearchResults.htm"
    parameters = {
        "zws-id": API_KEY,
        "price": price_range,
        "citystatezip": "Seattle, WA",
        "status": "for sale"
    }
    response = requests.get(endpoint, params=parameters)
    if response.status_code == 200:
        data = response.text
        # Parse the response data to extract the addresses
        # ...
        return data
    else:
        return None

houses = get_houses("500000-1000000")
if houses:
    print(houses)
else:
    print("An error occurred.")


