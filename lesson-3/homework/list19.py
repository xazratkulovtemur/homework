numbers=['1','1','2','3','4','5','3','4','1','7']
print(numbers)
a=input("Enter the number to replace with: ")
b=input("Enter the number to replace: ")

numbers.insert(numbers.index(a), b)
numbers.remove(a)
print(numbers)