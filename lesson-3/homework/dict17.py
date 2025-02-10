GPA = {
    "calculus": {1: 4},
    "microeconomics": {1: 4},  # we have dict in dict
    "acs": 3.5,
    "dsg": 3
}
dict2 = {1: 4}  # specified dict

# Check if dict2 is in the values of GPA
if dict2 in GPA.values():
    
    a=dict2.values()
    print(list(a))

else:
    print("dict2 is not in GPA values")