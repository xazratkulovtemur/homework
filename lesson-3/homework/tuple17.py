numbers=(1,1,2,3,4,5,3,4,1,7) 
print(numbers)
a=int(input("Enter the starting point: "))
b=int(input("Enter the ending point: "))
subtuple=numbers[a-1:b]
print("Maximum element in subtuple:",max(subtuple))