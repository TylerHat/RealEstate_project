import matplotlib.pyplot as plt
import array as arr
import numpy

file = open('housedata.txt', 'r')
read = file.readlines()


file_path = "housedata.txt"

def pr(needed_values):
    print(f"******************\n", (needed_values), "\n******************")

with open(file_path, 'r') as file:
        contents = file.read()

def tabulate_string(text):
    indent_level = 0
    result = ""
    for char in text:
        if char == '{':
            result += '{\n' + '\t' * (indent_level + 1)
            indent_level += 1
        elif char == '}':
            indent_level -= 1
            result += '\n' + '\t' * indent_level + '}'
        elif char == '[':
            result += '[\n' + '\t' * (indent_level + 1)
            indent_level += 1
        elif char == ']':
            indent_level -= 1
            result += '\n' + '\t' * indent_level + ']'
        elif char == ',':
            result += ',\n' + '\t' * indent_level
        else:
            result += char
    return result

tabulated_data= tabulate_string(contents) 

##pr(tabulated_data)

text_file = open("housedata_tabed.txt", "w")
n = text_file.write(tabulated_data)
text_file.close()



def correction_value_error(filename, word):
    with open(filename, 'r') as file:
        contents = file.read()
    contents = contents.replace(word, "valuIncreaseRate")
    with open(filename, 'w') as file:
        file.write(contents)

correction_value_error("housedata_tabed.txt", "valueIncreaseRate")

def increment_word_count(filename, word):

    with open(filename, 'r') as file:
        contents = file.read()
    count = 0
    start = 0
    while start < len(contents):
        start = contents.find(word, start)
        if start == -1:
            break
        count += 1
        contents = contents[:start] + f"{word}_{count}" + contents[start + len(word):]
        start += len(f"{word}_{count}")
    with open(filename, 'w') as file:
        file.write(contents)

increment_word_count("housedata_tabed.txt", "taxIncreaseRate")
increment_word_count("housedata_tabed.txt", "taxPaid")
increment_word_count("housedata_tabed.txt", "time")
increment_word_count("housedata_tabed.txt", "value")
increment_word_count("housedata_tabed.txt", "valuIncreaseRate")


def find_value_after_word(word, endchar):

    with open("housedata_tabed.txt", 'r') as file:
            string = file.read()

    index = string.find(word)
    if index == -1:
        return None
    index += len(word)
    start_index = string.find(':', index)
    end_index = string.find(endchar, start_index)
    if start_index == -1 or end_index == -1:
        return None
    if string[start_index + 1:end_index].strip() == 'null':
        return 0
    else:
        return string[start_index + 1:end_index].strip()

######## Section for Miscellaneous Info ############

city_address = find_value_after_word("city",',').strip().strip("\"")
state_address =  find_value_after_word("state",',').strip().strip("\"")
streetAddress =  find_value_after_word("streetAddress",',').strip().strip("\"")
zipCode =  find_value_after_word("zipcode",',').strip().strip("\"")
county = find_value_after_word("county",',').strip().strip("\"")
country = find_value_after_word("country",',').strip().strip("\"")
description_full = find_value_after_word("description",'\",').strip().strip("\"").split('\n')
description_full = ' '.join(description_full).replace('\t', '').replace(", ",",")

##use this for $/sqft 
house_sqft = float(find_value_after_word("livingArea",',').strip().strip("\""))
lotSize_sqft = float(find_value_after_word("lotSize",',').strip().strip("\""))


######## Section for Home Price Values ############
monthly_HoaFee = float(find_value_after_word("monthlyHoaFee",',').strip().strip("\""))
lastSoldPrice = float(find_value_after_word("lastSoldPrice",',').strip().strip("\""))
monthly_rentZestimate = float(find_value_after_word("rentZestimate",',').strip().strip("\""))
zestimateHouse = float(find_value_after_word("\"zestimate",',').strip().strip("\""))



######## Section for Taxes ############
tax_values= []
valuIncreaseRates = []
taxpaid = []
taxIncrease = []
comparable_years= []

year_start_tax = float(find_value_after_word("taxAssessedYear",","))
i1 =0
while i1 <=21:
    comparable_years.append(year_start_tax - i1)
    i1+=1
else:
    print()##"Year " + str(int(comparable_years[0])) + " data" )

i2=0
while i2<=21:
    tax_values.append(float(find_value_after_word("value_"+str(i2+1),",")))
    valuIncreaseRates.append(float(find_value_after_word("valuIncreaseRate_"+str(i2+1),"}")))
    taxpaid.append(float(find_value_after_word("taxPaid_"+str(i2+1),",")))
    taxIncrease.append(float(find_value_after_word("taxIncreaseRate_"+str(i2+1),",")))
    i2+=1
else:
    print('')


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

##Subplots for Tax Graphs

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(comparable_years, tax_values, '*-', color='red', markersize=5)
axs[0, 0].set_title('Tax Values by Year')
axs[0, 1].plot(comparable_years, valuIncreaseRates, '*-', color='green', markersize=5)
axs[0, 1].set_title('Tax Value Increase Rate by Year')
axs[1, 0].plot(comparable_years, taxpaid, '*-', color='blue', markersize=5)
axs[1, 0].set_title('Tax Paid by Year')
axs[1, 1].plot(comparable_years, taxIncrease, '*-', color='orange', markersize=5)
axs[1, 1].set_title('Tax Increase by Year')
plt.savefig('my_plots.png')

##plt.show()

######## Section for Analytics ############

""" Mortgage payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
where:

P is the principal (the amount of the loan)
r is the monthly interest rate (annual interest rate divided by 12)
n is the total number of payments (the number of years of the loan multiplied by 12)
Note that this equation assumes a fixed-rate mortgage. If you have an adjustable-rate mortgage, the mortgage payment may change over time."""

option_1 = input("Do you have the monthly interest rate or the yearly? (0 for monthly, 1 for yearly)")
if option_1 == 0:
    princible_rate = float(input("What is the interest rate?"))
    if princible_rate == "":
        princible_rate =3
    princible_rate = princible_rate/(12/100)
elif option_1 == 1:
    princible_rate = float(input("What is the interest rate?"))
    if princible_rate == "":
        princible_rate =3
    princible_rate = princible_rate/(100)
else:
    ##print("that is not a correct option")
    princible_rate = .03


initialpayment_Percent = int(input("How much (%) of the total value do you plan on puting down?"))/100
princible_loan_zest = float(zestimateHouse * (1-initialpayment_Percent))
numOfPayments = int(input("What is total amount of payments?"))

##print("princible" + princible_loan_zest)
print("princible_rate: " + str(princible_rate) +"\tinicialpayment%: " + str(initialpayment_Percent)+"\tprinc_loan_zestimate: " + str(princible_loan_zest)+ "\t# of payments: " + str(numOfPayments))

mortgage_payment_zest = (princible_loan_zest * initialpayment_Percent * princible_rate * (1 + princible_rate) ** numOfPayments)/((1 + princible_rate) ** (360-1))

pr(mortgage_payment_zest)


"""
Break-even point = Total cost of owning the property / Rental income per year


"""

breakEvenPoint = round(zestimateHouse/monthly_rentZestimate, 2)
print("zestimateHouse: "+ str(zestimateHouse)+ "\tmonthly_rentZestimate: "+ str(monthly_rentZestimate)+ "\nBreak Even Point: "+ str(breakEvenPoint))





"""
The cap rate is found by dividing the property's net operating expenses by its purchase price. You can find the cap rate by doing the following: 

Find your gross income by taking the average monthly rent for your property and multiplying it by 11.5. This will show the maximum amount you can make from the property, allowing for a two-week per year vacancy.

Then, subtract your monthly operating expenses ( utilities, taxes, maintenance) from your gross income to get your net income.

Divide your net income by the purchase price to find your cap rate.

Multiply the cap rate by 100 to find the percentage of your potential returns on the property.


"""