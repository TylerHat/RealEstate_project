class Financial:
    def __init__(self, expensesPerMonth=0.0,monthly_HoaFee=0.0, lastSoldPrice=0.0, monthly_rentZestimate=0.0, zestimateHouse=0.0, initialpayment_Percent=0.0,numOfPayments=0.0, princible_rate=0.0):
        self.monthly_HoaFee = monthly_HoaFee
        self.lastSoldPrice = lastSoldPrice
        self.monthly_rentZestimate = monthly_rentZestimate
        self.zestimateHouse = zestimateHouse
        self.initialpayment_Percent = initialpayment_Percent
        self.princible_loan_zest = princ_loan_zest(zestimateHouse, initialpayment_Percent)
        self.numOfPayments = numOfPayments
        self.princible_rate = princible_rate 
        self.mortgage_payment_zest =calculate_mortgage_payment((zestimateHouse*(1-initialpayment_Percent/100)), princible_rate, numOfPayments)
        self.breakevenpoint = breakevenpoint(zestimateHouse, monthly_rentZestimate)


def princ_loan_zest(zestimateHouse, initialpayment_Percent):
    try:
        result = (float(zestimateHouse) * (1-initialpayment_Percent))
        return result
    except:
        return 0


def mortgage_pay_zest(zestimateHouse, initialpayment_Percent, princible_rate, numOfPayments):
    """Mortgage payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
where:

P is the principal (the amount of the loan)
r is the monthly interest rate (annual interest rate divided by 12)
n is the total number of payments (the number of years of the loan multiplied by 12)
Note that this equation assumes a fixed-rate mortgage. If you have an adjustable-rate mortgage, the mortgage payment may change over time.
"""
    try:
        result = ((float(zestimateHouse) * (1-initialpayment_Percent)) * initialpayment_Percent * princible_rate * (1 + princible_rate) ** numOfPayments)/((1 + princible_rate) ** (360-1))
        return result
    except:
        return 0

def calculate_mortgage_payment(loan_amount, interest_rate, loan_term):
    '''
    This function calculates the monthly mortgage payment based on the loan amount, interest rate, and loan term.
    '''
    # Convert the interest rate from percentage to decimal
    interest_rate = interest_rate / 100 / 12

   
    # Calculate the monthly mortgage payment using the formula:
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    # where M is the monthly payment, P is the principal (loan amount), i is the monthly interest rate,
    # and n is the number of monthly payments (loan term in months)
    monthly_payment = loan_amount * (interest_rate * (1 + interest_rate) ** loan_term) / ((1 + interest_rate) ** loan_term - 1)

    # Round the monthly payment to two decimal places
    monthly_payment = round(monthly_payment, 2)

    return monthly_payment




def breakevenpoint(zestimateHouse, monthly_rentZestimate):
    """
    Break-even point = Total cost of owning the property / Rental income per year
    """
    try:
        result = round(zestimateHouse/monthly_rentZestimate, 2)
        return result
    except:
        return 0
    
def current_interest_rate():
    with open('interest_rates.txt', 'r') as file:
        lines = file.readlines()

    if len(lines) >= 2:
        second_last_line = lines[-4]
        print("The second to last line is:", second_last_line)
    else:
        print("The file does not have enough lines.")

time =360
rate=6.0
price = 214000
amount = calculate_mortgage_payment(price, rate, time)
print(amount)