file = open('housedata.txt', 'r')
read = file.readlines()

##print(read)
file_path = "housedata.txt"

def pr(needed_values):
    print(f"******************\n", (needed_values), "\n******************")

def extract_rent_zestimate(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        start = contents.find("rentZestimate") + len("rentZestimate")
        rent_zestimate = contents[start:start+7]
        return rent_zestimate



rent_zestimate = extract_rent_zestimate(file_path)

def extract_substring(input_string):
    start = input_string.index(":") + 1
    end = input_string.index(",")
    substring = input_string[start:end]
    return substring

zestimate_string= extract_substring(rent_zestimate)
pr(zestimate_string)

def count_characters(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        start = contents.find("taxAssessedValue")-1
        end = contents.find("staticUrl")
        tax_records = contents[start:end]
        return tax_records
tax_numbers= count_characters(file_path)

##pr(tax_numbers) 


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

tax_formate= tabulate_string(tax_numbers) 
pr(tax_formate) 

text_file = open("tax_data_raw.txt", "w")
n = text_file.write(tax_formate)
text_file.close()



def correction_value_error(filename, word):
    with open(filename, 'r') as file:
        contents = file.read()
    contents = contents.replace(word, "valuIncreaseRate")
    with open(filename, 'w') as file:
        file.write(contents)

correction_value_error("tax_data_raw.txt", "valueIncreaseRate")

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

increment_word_count("tax_data_raw.txt", "taxIncreaseRate")
increment_word_count("tax_data_raw.txt", "taxPaid")
increment_word_count("tax_data_raw.txt", "time")
increment_word_count("tax_data_raw.txt", "value")
increment_word_count("tax_data_raw.txt", "valuIncreaseRate")