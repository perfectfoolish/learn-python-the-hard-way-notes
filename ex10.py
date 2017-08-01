tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "put the formatting string and escape sequences together %r" % fat_cat
print "put the formatting string and escape sequences together %s" % fat_cat

# It does not work, go on reading the book, after study the while and for, the go
# back debug it
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
