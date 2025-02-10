numbers=(1,1,2,3,4,5,3,4,1,7) 
print(numbers)
a=int(input("Enter the number that each element in tuple will repeat that times: "))
numbers_list=list(numbers)
repeated_list=numbers_list*a
tuple_repeated=tuple(repeated_list)
print(tuple_repeated)
