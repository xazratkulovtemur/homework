numbers=[1,1,2,3,4,5,3,4,1,7]
print(numbers)
a=int(input("Select the position of element to remove from the list: "))
for num in numbers: 
    if (a-1)<=len(numbers)+1:
        numbers.remove(numbers[a-1])
        print(numbers)
        
    else: 
        print("No such position")
        break
#removing selected element from the list