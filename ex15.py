# import argv
from sys import argv
# use argv to get filename
script, filename = argv
# variable to store the content of the file is opened
txt = open(filename)

print "Here's your file %r:" % filename
# read the content from txt variable and print it
print txt.read()
print txt.close()

print "Type the filename again:"
file_again = raw_input(">")

# use raw_input method to get the file content
txt_again = open(file_again)

print txt_again.read()
print txt_again.close()
