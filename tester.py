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

filename = "file.txt"
word = "taxIncreaseRate"
increment_word_count(filename, word)


"""

def replace_in_file(filename, word_incrim):
    with open(filename, 'r') as file:
        contents = file.read()
        num = contents.count(word_incrim)
        
    with open(filename, 'w') as file:
        file.write(contents)

        for num in contents:
            ##start= contents.find(word_incrim)-1
            contents = contents.replace("taxIncreaseRate", "taxIncreaseRate_" +num)
            print(num)


replace_in_file('tax_data_raw copy.txt', "taxIncreaseRate")





"""
