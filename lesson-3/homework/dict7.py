GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    }
print(GPA)
a=input("Enter key to remove: ")
if a in GPA:
    GPA.pop(a)
    print("Removed key:", a)
else: 
    print("No such key")
print(GPA)