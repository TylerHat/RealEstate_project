from lxml import html
import requests
import unicodecsv as csv
import argparse
import random
from zillWebScrapNew import parse, organizetxtHome, clearing, getHouseInfoRIGHT, info2CSV, getHouseInfoLEFT




if __name__=="__main__":
	zipcode = input("Enter zipcode: ")
	sort = "newest"
	clearing()
	print("deleting old files")
	"""
	argparser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	argparser.add_argument('zipcode',help = '')
	sortorder_help = 
    available sort orders are :
    newest : Latest property details,
    cheapest : Properties with cheapest price
    
	argparser.add_argument('sort',nargs='?',help = sortorder_help,default ='Homes For You')
	args = argparser.parse_args()
	zipcode = args.zipcode
	sort = args.sort"""
	print ("Fetching data for %s"%(zipcode))
	parse(zipcode,sort)
	print ("Writing data to output file")
	organizetxtHome()
	info2CSV()
	print("Done printing to text file")
	

