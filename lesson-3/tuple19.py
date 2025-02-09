numbers=(1,1,2,3,4,5,3,4,1,7) 
print(numbers)
a=int(input("Enter the numebr to remove its first occurness: "))
numbers_list=list(numbers)
numbers_list.remove(a)
converted_to_tuple=tuple(numbers_list)
print("Tuple after modification:",converted_to_tuple)

#to remove or add item to tuple, first we convert it to list, then remove or add what we want, then again convert it to tuple