import requests

url = "https://zillow56.p.rapidapi.com/property"

querystring = {"zpid":"35413966"}

headers = {
	"X-RapidAPI-Key": "ccd2a329cdmsh48847502b1a3a8fp14a0f7jsn6db2e1605594",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


"""
import requests

def get_zestimate(zpid):
    API_KEY = "ccd2a329cdmsh48847502b1a3a8fp14a0f7jsn6db2e1605594"
    endpoint = "http://www.zillow.com/webservice/GetZestimate.htm"
    parameters = {
        "zws-id": API_KEY,
        "zpid": zpid
    }
    response = requests.get(endpoint, params=parameters)
    if response.status_code == 200:
        data = response.text
        # Parse the response data to extract the Zestimate and Zestimate history
        # ...
        return data
    else:
        return None

zestimate = get_zestimate(1234567890)
if zestimate:
    print(zestimate)
else:
    print("An error occurred.")
"""