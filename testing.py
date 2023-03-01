import matplotlib.pyplot as plt
import pandas as pd
import webbrowser
import numpy as np
from sklearn.linear_model import LinearRegression
from house import House



file = open('housedata.txt', 'r')
read = file.readlines()
file_path = "housedata.txt"
with open(file_path, 'r') as file:
        contents = file.read()

def pr(needed_values):
    print(f"******************\n", (needed_values), "\n******************")

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

text_file = open("housedata_tabed.txt", "w")
n = text_file.write(tabulated_data)
text_file.close()

def correction_value_error(filename, word, newword):
    with open(filename, 'r') as file:
        contents = file.read()
    contents = contents.replace(word, newword)
    with open(filename, 'w') as file:
        file.write(contents)

correction_value_error("housedata_tabed.txt", "valueIncreaseRate", "valuIncreaseRate")
correction_value_error("housedata_tabed.txt", '"zestimate":', '"HouseZestimate":')

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


def find_value(word, endchar):

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

description_full = find_value("description",'\",').strip().strip("\"").split('\n')
target_house = House(house_sqft= float(find_value("livingArea",',').strip().strip("\"")),
                     lotSize_sqft= float(find_value("lotSize",',').strip().strip("\"")),
                     city_address=find_value("city",',').strip().strip("\""),
                     state_address=find_value("state",',').strip().strip("\""),
                     streetAddress=find_value("streetAddress",',').strip().strip("\""),
                     zipCode=find_value("zipcode",',').strip().strip("\"\}"), 
                     county=find_value("county",',').strip().strip("\""), 
                     country=find_value("country",',').strip().strip("\""), 
                     description_full=' '.join(description_full).replace('\t', '').replace(", ",","))


##print(zestimateHouse)

target_house.house_sqft= float(find_value("livingArea",',').strip().strip("\""))
target_house.lotSize_sqft= float(find_value("lotSize",',').strip().strip("\""))


target_house.financial.monthly_HoaFee = float(find_value("monthlyHoaFee",','))
target_house.financial.lastSoldPrice = float(find_value("lastSoldPrice",',').strip().strip("\""))
target_house.financial.monthly_rentZestimate = float(find_value("rentZestimate",',').strip().strip("\""))
target_house.financial.zestimateHouse = float(find_value("HouseZestimate",','))


######## Section for Taxes ############
tax_values= []
valuIncreaseRates = []
taxpaid = []
taxIncrease = []
comparable_years= []
comparable_years2 = []
year_start_tax = float(find_value("taxAssessedYear",","))
i1 =0
while i1 <=21:
    comparable_years.append(year_start_tax - i1)
    i1+=1
else:
    debug=3
i3=0
while i3<=4:
    comparable_years2.append(year_start_tax + i3)
    i3+=1
else:
    debug =1
i2=0
while i2<=21:
    tax_values.append(float(find_value("value_"+str(i2+1),",")))
    valuIncreaseRates.append(float(find_value("valuIncreaseRate_"+str(i2+1),"}")))
    taxpaid.append(float(find_value("taxPaid_"+str(i2+1),",")))
    taxIncrease.append(float(find_value("taxIncreaseRate_"+str(i2+1),",")))
    i2+=1
else:
    debug=4



def predic_value(past_array, amount_to_predict):
    # Example input data
    data = np.array(past_array)
    leng =len(past_array)-4
    
    # Reshape the data into a 2D array with one column
    X = data.reshape(-1, 1)

    # Use the first 5 values as training data
    X_train = X[:leng]
    y_train = data[:leng]

    model = LinearRegression()
    model.fit(X_train, y_train)

    X_test = X[:amount_to_predict]
    y_pred = model.predict(X_test)

    return y_pred

future_tax_values = predic_value(tax_values, 5)
future_valuIncreaseRates = predic_value(valuIncreaseRates, 5)

plt.rcParams["figure.figsize"] = [7, 4.50]
plt.rcParams["figure.autolayout"] = False

##Subplots for Tax Graphs

fig, ax = plt.subplots()
##ax.plot(comparable_years3, greymatter, '*-', color='blue', label='y3')
ax.plot(comparable_years2, future_tax_values, 'b*-', label='linear regression estimate')
ax.plot(comparable_years, tax_values, 'r^-', label='Previous Tax Values')
# set the axis labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Tax Values')
ax.set_title('Predition of Tax Values in next 5 Years')

ax.legend(loc='best')

fig.savefig("my_plots_Tax_Values.png")

fig, ax2 = plt.subplots()
ax2.plot(comparable_years2, future_valuIncreaseRates, 'b*-', label='linear regression estimate')
ax2.plot(comparable_years, valuIncreaseRates, 'r^-', label='Previous Tax Increase Rates')
ax2.set_xlabel('Years')
ax2.set_ylabel('Tax Increase Rates')
ax2.set_title('Predition of Tax Change Rates in next 5 Years')

# add legend to the plot
ax2.legend(loc='best')

fig.savefig("my_plots_taxRates.png")

html_tab_TaxRate = []
html_tab_TaxValue = []
i=0
for year in range(int(year_start_tax+1),(int(year_start_tax)+5)):
    
    html_tab_TaxValue.append({
            "Year": int(year_start_tax+3)+i,
            "Tax Rage Change Prediction": round(future_tax_values[i], 3),
        })
    html_tab_TaxRate.append({
            "Year": int(year_start_tax+3)+i,
            "Tax Rage Change Prediction": round(future_valuIncreaseRates[i], 3),
        })
    i+=1
df_html_table_TaxRate = pd.DataFrame(html_tab_TaxRate)
table_TaxRate_html = df_html_table_TaxRate.to_html(classes='table table-stripped')
df_html_table_TaxValue = pd.DataFrame(html_tab_TaxValue)
table_TaxValue_html = df_html_table_TaxValue.to_html(classes='table table-stripped')


html_TaxRate_tb = df_html_table_TaxRate.to_html(classes='table table-stripped')


choice = ''"""
while choice != '0' and choice != '1':
    choice = input("Do you have the monthly interest rate or the yearly? (0 for monthly, 1 for yearly): ")
    if choice == 0:
        princible_rate = (input("What is the interest rate?") or 6)
        target_house.financial.princible_rate= float(princible_rate/(12/100))
        
    else:
        princible_rate = (input("What is the interest rate?") or 6)
        target_house.financial.princible_rate= float(princible_rate/(100))

target_house.financial.initialpayment_Percent= float(input("How much (%) of the total value do you plan on puting down?") or 20)/100, 
target_house.financial.numOfPayments = float(input("What is total amount of payments?") or 360)

target_house.financial.princible_loan_zest =  target_house.financial.zestimateHouse*(1-target_house.financial.initialpayment_Percent)

target_house.financial.initialpayment_Percent = float(input("How much (%) of the total value do you plan on puting down?") or 20)/100
target_house.financial.numOfPayments = float(input("What is total amount of payments?") or 360)

target_house.financial.princible_loan_zest = target_house.financial.zestimateHouse*(1-target_house.financial.initialpayment_Percent)"""
##target_house.financial.princible_loan_zest = float((target_house.financial.zestimateHouse) * (1.0-(target_house.financial.initialpayment_Percent))) 

while choice != '0' and choice != '1':
    choice = input("Do you have the monthly interest rate or the yearly? (0 for monthly, 1 for yearly): ")
    if choice == '0':
        target_house.financial.princible_rate = (input("What is the interest rate?") or 6)
        target_house.financial.princible_rate = float(target_house.financial.princible_rate/(12/100))
        
    else:
        target_house.financial.princible_rate = (input("What is the interest rate?") or 6)
        target_house.financial.princible_rate = float(target_house.financial.princible_rate/(100))

target_house.financial.initialpayment_Percent = float(input("How much (%) of the total value do you plan on puting down?") or 20)/100
target_house.financial.numOfPayments = float(input("What is total amount of payments?") or 360)

target_house.financial.princible_loan_zest = target_house.financial.zestimateHouse*(1-target_house.financial.initialpayment_Percent)
"""
================================================================================================================
================================================================================================================
================================================================================================================
================================================================================================================
"""



house_prop_data = []
expenses_per_month=200

total_rent_income = target_house.financial.monthly_rentZestimate*12
total_expenses = expenses_per_month *12
net_income = total_rent_income-total_expenses

##accumeulated values
accumulated_total_income = total_rent_income
accumulated_total_expense = total_expenses
accumulated_net_income = net_income
print(str(target_house.financial.zestimateHouse) + "     "+str(target_house.financial.princible_loan_zest))
##total_roi = ((zestimateHouse+ princible_loan_zest) +net_income)/(zestimateHouse+ princible_loan_zest)
total_roi = ((target_house.financial.zestimateHouse + target_house.financial.princible_loan_zest) +net_income)/(target_house.financial.zestimateHouse + target_house.financial.princible_loan_zest)

house_prop_data.append({
        "Year": int(year_start_tax)+2,
        "Total Income": round(total_rent_income, 3),
        "Total Expenses": round(total_expenses, 3),
        "Net Income": round(net_income, 3),
        "Total ROI": round(total_roi, 3),
        "Acc. Total Income": round(accumulated_total_income, 3),
        "Acc. Total Expence": round(accumulated_total_expense, 3),
        "Acc. Total Net Income": round(accumulated_net_income, 3)
    })


for year in range(int(year_start_tax),(int(year_start_tax)+10)):

    total_rent_income *= 1.03
    total_expenses *= 1.03
    net_income *= 1.03

    total_roi = ((target_house.financial.zestimateHouse + target_house.financial.princible_loan_zest) +net_income)/ \
        (target_house.financial.zestimateHouse + target_house.financial.princible_loan_zest)

    accumulated_total_income += total_rent_income
    accumulated_total_expense += total_expenses
    accumulated_net_income += net_income

    house_prop_data.append({
            "Year": int(year+3),
            "Total Income": round(total_rent_income, 3),
            "Total Expenses": round(total_expenses, 3),
            "Net Income": round(net_income, 3),
            "Total ROI": round(total_roi, 3),
            "Acc. Total Income": round(accumulated_total_income, 3),
            "Acc. Total Expence": round(accumulated_total_expense, 3),
            "Acc. Total Net Income": round(accumulated_net_income, 3)
        })
df = pd.DataFrame(house_prop_data)

html_yr_calc_tb = df.to_html(classes='table table-stripped')
  
df.to_csv('house30yrinvestment.csv')


img_path = 'my_plots.png'
image_tag = f'<img src="{img_path}" alt="image" width="1200">'

table_html = df.to_html(classes='table table-stripped')


full_html = """
<!DOCTYPE html>
<html>
<head>
	<title>Real Estate Report</title>
    <style>
		.img-container {
			display: flex;
			flex-direction: row;
            align-items: center;
			justify-content: center;
		}
		.img-container img {
			margin-right: 10px;
		}
        .label {
			text-align: Center;
			font-size: 16px;
			font-weight: bold;
		}
	</style>
    <style>
		.highlight {
			background-color: red;
			font-weight: bold;
		}
	</style>""" +f"""
</head>
<body>
	<br>
	<h3>This report was run for the Address: {target_house.location.full_address}</h3>
	<p>Description: {target_house.location.description_full}.</p><br><br>
    <h4>Monthly Rent Estimate: <span class="highlight">{target_house.financial.monthly_rentZestimate}</span>.<br><br>
    Princible Loan from Zestimate: <span class="highlight">{target_house.financial.princible_loan_zest}</span>&emsp;Last Sold Price: <span class="highlight">{target_house.financial.lastSoldPrice}</span>&emsp;<br>Zillow's Estimate on House Cost: <span style="color: blue;">{target_house.financial.zestimateHouse}</span><br>House Sqft: <span style="color: blue;">{target_house.house_sqft}</span><br>Zestimate Price/Sqft: <span style="color: blue;">{target_house.financial.zestimateHouse/target_house.house_sqft}</span></h4>
    <br><br>
    Monthyl HOA Fee: <span class="highlight">{target_house.financial.monthly_HoaFee}</span>
    <br><br>
    Mortgage payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
    &emsp;P is the principal (the amount of the loan)
    &emsp;r is the monthly interest rate (annual interest rate divided by 12)
    &emsp;n is the total number of payments (the number of years of the loan multiplied by 12)
    <br>Morgage Payment Estimate: <span style="color: blue;">{target_house.financial.mortgage_payment_zest}</span>
    <br><br>Break-even point = Total cost of owning the property / Rental income per year
    <br>BreakEven Point: <span style="color: blue;">{target_house.financial.breakevenpoint}</span>
    </p>
   
    <div class="img-container">
		<div>
			<img src="my_plots_taxRates.png" alt="Image 1">
			<p class="label">Esimated Future Tax Rate Changes:"""+table_TaxRate_html +"""</p>
		</div>
		<div>
			<img src="my_plots_Tax_Values.png" alt="Image 2">
			<p class="label">Esimated Future Tax Values: """+ table_TaxValue_html+""":</p>
		</div>
	</div>
    <div>
    <p class="label">"""+ table_html +"""</p>
    </div>
</body>
</html>
"""

##full_html = f"""<h1>My House</h1><ul><li>Cost: """+{target_house.financial.breakevenpoint}+"""</li><li>Color: {target_house.location.full_address}</li></ul>"

# Save the HTML code to a file
with open('result.html', 'w') as f:
    f.write(full_html)

# open the HTML page in a new tab in the default web browser
webbrowser.open_new_tab("result.html")