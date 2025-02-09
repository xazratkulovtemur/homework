numbers=(1,1,2,3,4,5,3,4,1,7) 
print(numbers)
element_to_check=int(input("Enter the number to check its indices: "))
indices=[i for i,x in enumerate(numbers) if x == element_to_check]
print("Indices of element", element_to_check, " in the tuple:", indices)