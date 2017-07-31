name = 'Zed A.Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "He's %r inches tall and got %r eyes." % (height, eyes)

print "His height is %f m" % 1.83
print "His height is %.2f m" % 1.83

print "2 inches equal to %.2f cm" % (2 * 2.54)
print "1 lb equal to %.7f kg" % (1 * 0.4535924)
print "2 lb equal to %.7f kg" % round(2 * 0.4535924)
