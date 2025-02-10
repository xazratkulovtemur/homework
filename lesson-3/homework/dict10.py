GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    }
print(GPA)
a=input("Enter the course: ") #ask user ot write key
if a in GPA: 
    value=GPA[a]
    print(a,",",value)
else:  
    print("No such course")