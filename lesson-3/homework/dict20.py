GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    }
print(GPA)
values=GPA.values()
keys=sorted(GPA.keys())
sorted_gpa={key: GPA[key] for key in keys}
print(sorted_gpa)
