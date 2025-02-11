GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    }
print(GPA)
sorted_by_value=dict(sorted(GPA.items(), key=lambda item: item[1])) #helps to sort by elements
print(sorted_by_value)
