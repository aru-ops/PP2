# Function returning a boolean
def myFunction():
    return True

print(myFunction())  # True

if myFunction():
    print("YES!")
else:
    print("NO!")

# Using built-in function isinstance()
x = 200
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False
