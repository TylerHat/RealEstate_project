import requests


url = "https://zillow56.p.rapidapi.com/property"

querystring = {"zpid":"35413966"}

headers = {
	"X-RapidAPI-Key": "ccd2a329cdmsh48847502b1a3a8fp14a0f7jsn6db2e1605594",
	"X-RapidAPI-Host": "zillow56.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
text_file = open("housedata.txt", "w")
n = text_file.write(response.text)
text_file.close()

"""
Gross Rent Multiplier (GRM) = Sales Price / Gross Rent

GRM can be used as a quick and rough estimate of the potential return on investment (ROI) for a rental property. 
The higher the GRM, the lower the potential return, and vice versa.

To calculate the potential ROI, you can use the following formula:

ROI = (Annual Rent - Annual Expenses) / Purchase Price

Annual expenses include property taxes, insurance, maintenance and repair costs, 
and other expenses associated with owning a rental property.

It's important to note that this is just a rough estimate and does not take into account other factors such as appreciation, 
financing costs, inflation, and market conditions, which can all impact the profitability of a real estate investment. 
A more comprehensive analysis would require a detailed analysis of all the relevant financial and market data.

"""
