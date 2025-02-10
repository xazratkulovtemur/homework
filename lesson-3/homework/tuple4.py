numbers=(1,1,2,3,4,5,3,4,1,7) 
a=int(input("Enter the number to check if it is in tuple: "))
for num in numbers:
    if a in numbers:
        print("Yes it is in tuple")
    else: 
        print("No, it is not in tuple")
    break
    