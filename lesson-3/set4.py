numbers={frozenset({1,2}),3,4,5,6,7,8}
sub_set=frozenset({1,2})
is_subset=sub_set in numbers
print(is_subset)

#since sets are unhashable, we cannot write in set. to check if it is subset, we can you frozenset({1,2})