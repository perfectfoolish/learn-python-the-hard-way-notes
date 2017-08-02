def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def boys_and_girls(boy_count, girl_count):
    print "There will be %d boys come to party" % boy_count
    print "There will be %d girls come to party" % girl_count

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from script:"
amount_of_cheese = 10
amount_of_crackers = 50
# call the function with variables from script
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# call the function with math
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math"
# call the function with combining the variables with math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

input_amount_of_cheese = int(raw_input("Input the amount of cheese:"))
input_amount_of_crackers = int(raw_input("Input the amount of crackers:"))
input_amount_of_boy = int(raw_input("Input the amount of boy:"))
input_amount_of_girl = int(raw_input("Input the amount of girl:"))
cheese_and_crackers(input_amount_of_cheese, input_amount_of_crackers)
boys_and_girls(input_amount_of_boy, input_amount_of_girl)
