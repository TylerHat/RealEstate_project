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


######## Section for Home Price Values ############

monthly_HoaFee = find_value_after_word("monthlyHoaFee",',').strip().strip("\"")
lastSoldPrice = find_value_after_word("lastSoldPrice",',').strip().strip("\"")
monthly_rentZestimate = find_value_after_word("rentZestimate",',').strip().strip("\"")
zestimateHouse = find_value_after_word("\"zestimate",',').strip().strip("\"")


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
    print("Year " + str(int(comparable_years[0])) + " data" )

i2=0
while i2<=21:
    tax_values.append(float(find_value_after_word("value_"+str(i2+1),",")))
    valuIncreaseRates.append(float(find_value_after_word("valuIncreaseRate_"+str(i2+1),"}")))
    taxpaid.append(float(find_value_after_word("taxPaid_"+str(i2+1),",")))
    taxIncrease.append(float(find_value_after_word("taxIncreaseRate_"+str(i2+1),",")))
    i2+=1
else:
    print('error in array filling')


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