numbers=(1,1,2,3,4,5,3,4,1,7) 
a=len(numbers)
numbers_list=list(numbers)
sub_list1=numbers_list[:a/2]
sub_list2=numbers_list[a/2:]
joined_list=sub_list1+sub_list2
print(joined_list)


