GPA ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    }
print(GPA)
print("Now, we count how many time 4 repeted.")
count4=0
for values in GPA.values(): # this specifies values in GPA.values()
    if values==4:
        count4 +=1 #if so, plus 1
    else: 
        count4+=0

print(count4)

