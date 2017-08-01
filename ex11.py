print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "What is your first name?",
first_name = raw_input()
print "What is your last name?",
last_name = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r %r and %r heavy." % (first_name, last_name, weight)

x = raw_input("please input a number:")
y = raw_input("please input a number:")

if x >= y:
    print x
else:
    print y
