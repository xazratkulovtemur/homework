numbers=[1,1,2,3,4,5,3,4,1,7]
print(numbers)
a=int(input("Enter the number to check: "))

indices = [i for i,x in enumerate(numbers) if x==a]
print("Indices of element", a, " in the list:", indices)