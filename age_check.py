age = raw_input("age: ")

def check_age(age):
  while True:
    if age.isdigit():
      return age
    else:
      age = raw_input("You need to enter your age: ")

age = check_age(age)
print age
