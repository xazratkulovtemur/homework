def check(func):
    def wrapper(a,b): #2 variables
        if b==0:  #considering if denominator is 0
            return "Denominator cannot be 0!"
        return func(a,b)
    return wrapper 

@check  #connecting two def
def div(a,b):
    return a/b

print(div(3,2))
print(div(6,0)) #examples
