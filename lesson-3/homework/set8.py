numbers={1,2,3,4,5,6,7,8}
print(numbers)
a=int(input("Enter the number to remove: "))
if a in numbers: 
    numbers.remove(a)
    print("Set after removing element:", numbers)
else: 
    print("Not such element in set.")
