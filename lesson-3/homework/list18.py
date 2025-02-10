num=[1,2,3,4,5,6,7,8,9]
sub_num=[1,2,9]
num_str=''.join(map(str, num))
sub_num_str=''.join(map(str, sub_num))
if sub_num_str in num_str: 
    print("Yes sublist is inside the list")
else: 
    print("No, sublist is not inside the list")

    #not finished