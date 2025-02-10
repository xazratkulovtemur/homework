GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    } #this is my dictionary
print("Original dictionary:",GPA)
swapped_GPA= {}
for key, value in GPA.items():  
    swapped_GPA[value]=key

print("Swapped dictionary:s",swapped_GPA)

