#Datatype questions


#problem1 
"""
a=float(input("Enter decimal number:"))
print(f"{a:.2f}")

"""

#problem2
"""
a=int(input("Enter the first number: "))
b=int(input("ENter second number: "))
c=int(input("ENter third number: "))

if a<b and b<c: 
    print(f"{c} is the largest, and {a} is the smallest")
if a>b and b>c:
    print(f"{a} is the largest, and {c} is the smallest")
if a<c and c<b:
    print(f"{b} is the largest, {a} is the smallest")
if b<c and c<a:
    print(f"{a} is largest, and {b} is smallest")
if c<a and a<b:
    print(f"{b} is the largest, and {c} is the smallest")
if b<a and a<c:
    print(f"{c} is largest, and {b} is smallest")

"""

#problem3
"""
a=float(input("Enter distance in meters: "))
k=a/1000
c=a*1000
print(f"{a} meters are: \n {k} kilometers and {c} centimeters")

"""

#problem 4
"""
a=int(input("Enter the number: "))
b=int(input("Enter the divisor: "))
x,y=divmod(a,b)
print(f"Answer is  {x} and remainder is {y}") 
"""
#problem5
"""
a=float(input("Enter degree in Celsius: "))
f=a*9/5+32
print(f"Temprature in Faranheit is {f}")
"""
#problem6



#problem7
"""
a=int(input("Enter the number: "))
if a%2==0:
    print("EVen number")
else: 
    print("Odd number")
"""

#STring questions

#problem1
"""
a=str(input("Enter your name: "))
b=int(input("Enter your year of birth:"))
age=2025-b
print("Hey,  {} . You are {} years old".format(a, age) )
"""

#problem2