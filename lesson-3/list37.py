numbers=[1,1,2,3,4,-5,3,-4,-1,7]
negative_sum=0
for num in numbers: 
    if num<0:
        negative_sum += num
print("Sum of the negative numbers:", negative_sum)