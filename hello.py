#Hello World example for python code . Enter your name

name = input("What is your name? ")
name=name.strip().title() # to strip the empty space in str (str is data type String in Python)
#name=name.title()
# Taking name into the variable
print("hello ,", end="") # the parameter like end=,sep= are called as named parameter. By default end="\n" which goes to next line.
#print("hello ",name, sep="??")
print(name)
# You can use " " or ' ' python consider both same

#print("hello , \"friend \" ") scaping " " and trying to show "friend"

# modern way of showing the hello , Vibhas

print(f"hello Mr,{name}") # every thing is under the " " and { } shows a special value. Note  the print function starts with f to tell the python

# you can split the string using split(" ") and assign them to variable first and last

first, last = name.split()

print(f"Your first name is {first} and last name is {last}" )