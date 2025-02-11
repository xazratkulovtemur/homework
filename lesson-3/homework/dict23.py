GPA_me ={
    "calculus": 4,
    "microeconomics": 4,
    "acs": 3.5,
    "dsg": 3
    }
GPA_her = {
    "calculus": 4,
    "microeconomics1": 4,
    "acs1": 3.5,
    "dsg": 3
}
common_keys= []
for key in GPA_me: 
    if key in GPA_her:
        common_keys.append(key)
if common_keys[0]!=None:
     print("Common keys:", common_keys)
else: 
    print("No common keys")
    

   