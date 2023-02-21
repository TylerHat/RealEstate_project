m = 3
n = 2
p = m ** n
print ("On solving the exponent, we get ", p)


######## Section for Analytics ############

""" Mortgage payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
where:

P is the principal (the amount of the loan)
r is the monthly interest rate (annual interest rate divided by 12)
n is the total number of payments (the number of years of the loan multiplied by 12)
Note that this equation assumes a fixed-rate mortgage. If you have an adjustable-rate mortgage, the mortgage payment may change over time."""


princible_rate = .03

zestimateHouse = 190000

initialpayment_Percent = .2
##princible_loan_zest = 152000
numOfPayments = 360

princible_loan_zest = float(zestimateHouse * (1-initialpayment_Percent))

print(princible_loan_zest)
print(princible_rate)
print(initialpayment_Percent)
print(princible_loan_zest)
print(numOfPayments)



mortgage_payment_zest_up = (princible_loan_zest * initialpayment_Percent * princible_rate * (1 + princible_rate) ** numOfPayments)
mortgage_payment_zest_down = ((1 + princible_rate) ** (360-1))

print("mortgage_payment_zest_up" + str(mortgage_payment_zest_up))
print("mortgage_payment_zest_down" + str(mortgage_payment_zest_down))

print(mortgage_payment_zest_up/mortgage_payment_zest_down)