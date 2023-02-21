import requests


"""
pull api key info from c drive txt file
"""
api_file_path =open(r"C:/Users/Tyler/Desktop/ZillowAPIKey.txt").read()

url = "https://zillow56.p.rapidapi.com/property"

querystring = {"zpid":"57283238"}

headers = {
	"X-RapidAPI-Key": api_file_path,
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

##print(response.text)

text_file = open("housedata.txt", "w")
n = text_file.write(response.text)
text_file.close()
