
x=int(input("What is your x?")) # we are using int() the inner most function take string and converted to int

y=int(input("What is your y?"))

# z=int(x) + int(y) one way to use a variable z and print the value.

print(x+y)


a=float(input("What is your a?"))
b=float(input("What is your b?"))

z=round(a+b)

print(z)

# formatting the output in a pattern like for 100000 to readable 100,000
print(f"{z:,}")

u=float(input("What is your u ?"))
v=float(input("What is your v ?"))

s=round(u/v,2)

print(s)