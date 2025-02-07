sentence=str(input("Enter the sentence: "))
if any(char.isdigit() for char in sentence):
    print("True")
else:
    print("False" )