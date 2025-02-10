numbers={1,2,3,4,5,6,7,8}
a=int(input("Enter the element to add it to SET :"))
if a not in numbers:
    numbers.add(a) 
    print(numbers)
else: 
    print("Element already exits!")