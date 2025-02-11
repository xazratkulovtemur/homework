GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 2
    }
filtered={}
for key, value in GPA.items():
    if value > 3:
        filtered[key]=value #pair keys and values

print(filtered)

