class Locaction:
    def __init__(self, city_address=None, state_address=None, streetAddress=None, zipCode=None, county=None, country=None, description_full=None):
        self.city_address = city_address
        self.state_address = state_address
        self.streetAddress = streetAddress
        self.zipCode = zipCode
        self.county = county
        self.country = country
        self.description_full = description_full
        self.full_address = streetAddress + ", " + city_address + ", " + county +" "+ zipCode +" " + country





