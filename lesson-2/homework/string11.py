#if any character is digit in the sentence

sentence=str(input("Enter the sentence: "))
if any(char.isdigit() for char in sentence):
    print("True")
else:
    print("False" )