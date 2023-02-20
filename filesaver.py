text = '''Hello
World
This is a multi-line string
'''

# Split the text into an array of lines
lines = text.split('\n')

# Join the lines into a single string, separated by commas
joined_text = ', '.join(lines)

print(joined_text)
