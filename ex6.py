# x is a variable, its content use formatting prints
x = "There are %d types of people." % 10
# a string variable
binary = "binary"
# a string variable
do_not = "don't"
# y is a variable, its content use formatting prints with two variable
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# put one string into another string
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# a string variable
w = "This is the left side of..."
# a string variable
e = "a string with a right side."

# connect string
print w + e
