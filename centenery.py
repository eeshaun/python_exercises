
from datetime import datetime
now = datetime.now()
print now
year = now.year
print year


name = raw_input("name: ")
age = raw_input("age: ")

def check_name(name):
  x = 1
  while x >= 0:
    if name.isalpha():
      x -= 1
      return name
    else:
      name = int(raw_input("You need to enter your name: "))

name = check_name(name)
print name


def check_age(age):
  while True:
    if age.isdigit():
      return age
    else:
      age = raw_input("You need to enter your age: ")

age = check_age(age)
print age
