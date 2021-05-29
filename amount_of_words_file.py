# Counting the amount of words in a text file

file = open(input('File name: '), 'r')
text = file.read()
output = text.split()
print(len(output))
