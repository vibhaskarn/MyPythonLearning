def hello(to="world"): # here to=world will take the value world if hello() got called where it takes default value as hello. hello(name) allowing to take the value passed in to 
    print("hello ,", to)

hello()
name = input("What is your name? ")
hello(name)
#print(name)