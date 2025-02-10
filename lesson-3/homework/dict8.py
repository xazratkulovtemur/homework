GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    } #my DICT
print(GPA)
a=input("Do you want to clear dictionary: ")
if a=='yes':
    cleared_dict=GPA.clear()  
    print(cleared_dict)
    print(type(cleared_dict))
else: 
    print("Check you said yes!")
