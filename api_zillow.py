import requests


"""
pull api key info from c drive txt file
"""
api_file_path =open(r"ZillowAPIKey.txt").read()

url = "https://zillow56.p.rapidapi.com/property"

querystring = {"zpid":"35413966"}

headers = {
	"X-RapidAPI-Key": api_file_path,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


text_file = open("housedata.txt", "w")
n = text_file.write(response.text)
text_file.close()


url = "https://u-s-economic-indicators.p.rapidapi.com/api/v1/resources/prime-rate-daily"

headers = {
	"X-RapidAPI-Key": api_file_path,
	"X-RapidAPI-Host": "u-s-economic-indicators.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

text_file = open("interest_rates.txt", "w")
n = text_file.write(response.text)
text_file.close()