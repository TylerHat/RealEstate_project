
#from location import Locaction
#from financial import Financial
"""
class House:
    def __init__(self, house_sqft=0.0, lotSize_sqft=0.0,  city_address="None", state_address="None", streetAddress="None", zipCode="None", county="None", country="None", description_full="None", monthly_HoaFee=0.0, lastSoldPrice=0.0, monthly_rentZestimate=0.0, zestimateHouse=0.0, initialpayment_Percent=0.0,numOfPayments=0.0, princible_rate=0.0):
        self.house_sqft = house_sqft
        self.lotSize_sqft = lotSize_sqft
        self.financial = Financial(monthly_HoaFee, lastSoldPrice, monthly_rentZestimate, zestimateHouse, initialpayment_Percent,numOfPayments, princible_rate)
        self.location = Locaction(city_address, state_address, streetAddress, zipCode, county, country, description_full)

"""
class House:
    def __init__(self, address, zpid, cost, link, town, daysOnZill, baths, beds, sqft):
        self.address = address
        self.zpid = zpid
        self.cost = cost
        self.town = town
        self.link = link
        self.daysOnZill = daysOnZill
        self.baths = baths
        self.beds = beds
        self.sqft = sqft


