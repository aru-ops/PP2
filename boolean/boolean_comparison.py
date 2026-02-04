# Using bool() function to evaluate values
print(bool("Hello"))  # True
print(bool(15))       # True

x = "Hello"
y = 15
print(bool(x))        # True
print(bool(y))        # True

# Values that are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Custom object example
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  # False
