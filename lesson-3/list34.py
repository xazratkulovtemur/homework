numbers=[1,1,2,3,4,5,3,4,1,7]
a=int(input("Enter the the numebr so that I rotate the list by these positions: "))
copied=numbers.index[:a]
deleted_numbers=numbers.remove(copied)
print(deleted_numbers)

#not finished