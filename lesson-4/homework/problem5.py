password=str(input("Let's create password: "))
if len(password)<8:
    print("Too short")
if not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter!")
if len(password)>=8 and any(char.isupper() for char in password):
    print("Password is strong!")