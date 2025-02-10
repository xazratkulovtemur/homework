GPA ={
    "calculus": {1,4},
    "microeconomics": {1,4}, #we have dict in dict
    "acs": 3.5,
    "dsg": 3
    }
dict2={1,4} #specified dict
if dict2 in GPA.values() or GPA.keys():    #to check if subdict in GPA`s keys or values
    print("Yes, it is nested dictinary")
else: 
    print("no, it is not nested dictinary")