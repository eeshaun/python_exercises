from datetime import datetime
name = raw_input("What is your name?: ")
age = int(raw_input("How old are you?: "))
print "Name: %s" % name
print "Age: %d" % age

years_to_100 = 100 - 32
print "Years to 100: %d" % years_to_100
now = int(datetime.now())
print now.year
centenary = now + (100 - age)
print centenary
