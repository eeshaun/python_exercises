name = raw_input("name: ")

def check_name(name):
  while True:
    if name.isalpha():
      return name
    else:
      name = int(raw_input("You need to enter your name: "))

name = check_name(name)
print name
