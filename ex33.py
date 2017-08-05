numbers = []

def build_list(length, step):
    i = 0
    while i < length:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

for i in range(1, 6):

    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now:", numbers
    print "At the bottom i is %d" % i

#build_list(5, 2)
print "The numbers:"

for num in numbers:
    print num
