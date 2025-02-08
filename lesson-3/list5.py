numbers=[1,2,3,4,5,6,7,8,9]
a=int(input("Enter the number to check: "))
for int in numbers:
    if a in numbers:
        print("Yes the number is in the list")
        break
    else: 
        print("No, the number is not in the list")
        break