numbers=[1,1,2,3,4,5,3,4,1,7]
print(numbers)
n=len(numbers)
a=int(input("Enter the number: "))
moved=numbers[a-n:]
remained=numbers[:a-n]
rotated=moved+remained
print(rotated)