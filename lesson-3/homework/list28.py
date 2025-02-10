numbers=[1,1,2,3,4,5,3,4,1,7]
a=int(input("Enter starting point for sublist: "))
b=int(input("Enter ending point for sublist: "))
sub_numbers=numbers[a-1:b]
print(sub_numbers)
min_element=min(sub_numbers)
print("Minimum elemt in sublist is", min_element)

#finding minimum element in sublist