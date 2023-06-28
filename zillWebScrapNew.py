from lxml import html
import requests
import unicodecsv as csv
import argparse
import random
import os
import csv
from house import House

def clearing():
	if os.path.exists("outputfromHTML.txt"):
		os.remove("outputfromHTML.txt")
	if os.path.exists("sandbox.txt"):
		os.remove("sandbox.txt")
	if os.path.exists("output_file_1.txt"):
		os.remove("output_file_1.txt")
	if os.path.exists("houseseporated.txt"):
		os.remove("houseseporated.txt")

	headers = ["Address", "Town","Zpid", "Cost","Beds", "Baths", "sqft","Days on Zillow",  "Link"]

	with open("output.csv", "w", newline="") as csvfile:
		writer = csv.writer(csvfile)

		# Write the header row
		writer.writerow(headers)

def parse(zipcode,filter=None):

	userAgents=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/113.0.1774.57",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57",
	]

	data_request = requests.get('https://www.whatismybrowser.com', headers={'User-Agent': random.choice(userAgents)})

	if filter=="newest":
		url = "https://www.zillow.com/homes/for_sale/{0}/0_singlestory/days_sort".format(zipcode)
	elif filter == "cheapest":
		url = "https://www.zillow.com/homes/for_sale/{0}/0_singlestory/pricea_sort/".format(zipcode)
	else:
		url = "https://www.zillow.com/homes/for_sale/{0}_rb/?fromHomePage=true&shouldFireSellPageImplicitClaimGA=false&fromHomePageTab=buy".format(zipcode)
	
	for i in range(5):
		# try:
		headers= {
					'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'accept-encoding':'gzip, deflate, sdch, br',
					'accept-language':'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
					'cache-control':'max-age=0',
					'upgrade-insecure-requests':'1',
					'user-agent': random.choice(userAgents)
		}
		response = requests.get(url,headers=headers)
		print(response.status_code)
		#print(response.text)

		datatext = response.text

		with open("outputfromHTML.txt", "w", encoding="utf-8") as file: file.write(datatext)
		with open("outputfromHTML.html", "w", encoding="utf-8") as file: file.write(datatext)
		
		
		return 

	
def organizetxtHome(file="outputfromHTML.txt"):
	target_string = "</div></article></div></div></li><li"
	dev_tester = "sandbox.txt"
	counter = 0
	#snipt to find how many houses are in text file
	# 
	with open(str(file), "r+", encoding="utf-8") as file_1:
		for line in file_1:
			counter += line.count(target_string)
			
			

		print("houses found: " + str(counter))
	#finds target string and stores it into a variable	
	#with open(file, "r+", encoding="utf-8") as file:
	
	output_text = ""
	count=0
	line_numbers=[]

	search_string = "</div></article></div></div></li><li"
	line_numbers = []
	output_lines = []

	with open("outputfromHTML.txt", "r", encoding="utf-8") as input_file:
		for line_number, line in enumerate(input_file, start=1):
			if search_string in line:
				line_numbers.append(line_number)
				line = line.replace(search_string, search_string + "houseISFOUND\n")
			output_lines.append(line)

	with open("houseseporated.txt", "w", encoding="utf-8") as output_file:
		output_file.writelines(output_lines)

	input_file = "houseseporated.txt"
	output_file = "sandbox.txt"

	with open(input_file, "r", encoding="utf-8") as file:
		lines = file.readlines()

	matching_lines = [line for line in lines if "houseISFOUND" in line]

	with open(output_file, "w", encoding="utf-8") as file:
		file.writelines(matching_lines)

def getHouseInfoRIGHT(lineNum, start_substring, end_substring,file="sandbox.txt" ):
	with open(file, "r", encoding="utf-8") as file:
		lines = file.readlines()

	if len(lines) >= lineNum:
		line_2 = lines[(lineNum-1)]
		line_2 = line_2.strip()  # Optional: Remove leading/trailing whitespace

		# Print or use the value of line 2 as needed
		#print(line_2)
	else:
		print("The file does not any records")

	text = line_2

	#start_substring = "\"streetAddress\":\""
	#end_substring = "\",\""

	start_index = text.find(start_substring)
	end_index = text.find(end_substring, start_index + len(start_substring))

	#print(f"start: {start_index}\t finish {end_index }")
	if start_index != -1 and end_index != -1:
		start_index += len(start_substring)
		result = text[start_index:end_index].strip()

		return(result)
	else:
		print("Substring not found in the text")

def getHouseInfoLEFT(lineNum, start_substring, end_substring_will_lookleft,file="sandbox.txt" ):
	with open(file, "r", encoding="utf-8") as file:
		lines = file.readlines()

	if len(lines) >= lineNum:
		line_2 = lines[(lineNum-1)]
		line_2 = line_2.strip()  # Optional: Remove leading/trailing whitespace

		# Print or use the value of line 2 as needed
		#print(line_2)
	else:
		print("The file does not any records")

	text = line_2

	start_index = text.find(start_substring)
	if start_index != -1:
		end_index = text.rfind(end_substring_will_lookleft, 0, start_index)
		if end_index != -1:
			#end_index += len(end_substring_will_lookleft)
			result = text[end_index + len(end_substring_will_lookleft):start_index]
			return(result)
		else:
			print(f"Substring {end_substring_will_lookleft} not found before {start_substring}")
	else:
		print(f"Substring {start_substring} not found")

def info2CSV():


	counter = 0
	#snipt to find how many houses are in text file
	# 
	with open("sandbox.txt", "r+", encoding="utf-8") as file_1:
		for line in file_1:
			counter += line.count("houseISFOUND")
	for i in range(1, counter):
		"""
		Order of class House self, address, zpid, cost, town, link, daysOnZill, baths, beds, sqft
		"""
		house = House(getHouseInfoRIGHT(i, "\"streetAddress\":\"", "\",\""),
		#Zpid
				getHouseInfoRIGHT(i,"\"property-card\" id=\"zpid_","\" class=\"StyledPropertyCard-c11n"),
				#cost
				getHouseInfoRIGHT(i,"$","</span></div>"),
				#Link
				getHouseInfoRIGHT(i,"property-card-data\"><a href="," data-test"),
				#Town
				getHouseInfoRIGHT(i,"\"addressLocality\":\"","\",\""),
				#Days on Zillow
				getHouseInfoLEFT(i,"on Zillow","\">"),
				#Baths
				getHouseInfoRIGHT(i,"bds</abbr></li><li><b>","</b>"),
				#Beds
				getHouseInfoLEFT(i,"</b> <abbr>bds</abbr></li><li><b>","<b>"),
				#sqft
				getHouseInfoRIGHT(i,"<abbr>ba</abbr></li><li><b>","</b>"),
				)		
		#print("address: "+ house.address)
		#print("zpid: "+ house.zpid)
		#print("town: "+ str(house.town))
		#print("cost: "+ house.cost)
		#print("link: "+ str(house.link))
		#print("daysonZill: "+ str(house.daysOnZill))
		#print("baths: "+ str(house.baths))
		#print("beds: "+ str(house.beds))
		#print("sqft: "+ str(house.sqft))
		#print("address: "+ house.address)




		#print("address: " + str(house.address))
		#print("zpid: "+str(zpid))
		#print("cost: "+str(house.cost))
		#["Address", "Town","Zpid", "Cost","Beds", "Baths", "sqft","Days on Zillow",  "Link"]
		data = [[house.address, house.town, house.zpid, house.cost, house.beds, house.baths, house.sqft, house.daysOnZill, house.link]]
		print(data)
		record = [[house.address, house.zpid, house.town, house.cost, house.link, house.daysOnZill, house.baths, house.beds, house.sqft]]
		address_exists = False
		with open("output.csv", "r", newline="") as csvfile_1:
			
			reader = csv.reader(csvfile_1)
			for row in reader:
				if row and row[0] == house.address:
					address_exists = True
					break

		if address_exists:
			print("Record with the same address already exists in the CSV file. Skipping...")
		else:
			# Append the data row to the CSV file
			with open("output.csv", "a", newline="") as csvfile_2:
				writer = csv.writer(csvfile_2)
				writer.writerows(record)
		print("Data added to the CSV file.")

	#print("CSV file created successfully.")