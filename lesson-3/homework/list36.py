numbers=[1,1,2,3,4,5,-3,4,1,-7]
positive_sum=0
for num in numbers:
    if num>0:
        positive_sum+= num

print("Sum of the positive numbers:", positive_sum)