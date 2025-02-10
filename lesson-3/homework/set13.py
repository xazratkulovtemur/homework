numbers={1,2,3,4,5,6,7,8}
a=int(input("Enter the element to pop it out: "))
if a in numbers: 
    b=numbers.pop()
    print("This is new SET:", numbers, " and this is removed element:", b)
else:
    print("No such element exist")

