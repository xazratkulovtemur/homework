numbers=(1,1,2,3,4,5,3,4,1,7) 
print(numbers)
a=len(numbers)
numbers_list=list(numbers)
sub_list1=numbers_list[:a//2]
sub_tuple1=tuple(sub_list1)
sub_list2=numbers_list[a//2:]
sub_tuple2=tuple(sub_list2)
last_list=[]
last_list.append(sub_tuple1)
last_list.append(sub_tuple2)
last_tuple=tuple(last_list)
print(last_tuple)


