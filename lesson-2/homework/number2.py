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