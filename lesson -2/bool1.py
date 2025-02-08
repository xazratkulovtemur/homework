username=str(input("Enter your username: "))
password=str(input("Enter password: "))
if not bool((username and password).strip()): 
    print("Please enter your username and password!")
else: 
    print(f"Your username: {username} \n Your password: {password}")
    