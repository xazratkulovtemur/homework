numbers=[1,1,2,3,4,5,3,4,1,7]
print(numbers)
fruits=['banana','apple', 'cherry']
print(fruits)
print("Do you want to sort and merge them?")
answer=input()
if answer=="yes":

    sorted_numbers=sorted(numbers)
    sorted_fruits=sorted(fruits)
    print(sorted_numbers+sorted_fruits)
else: 
    print('Check you wrote "yes"')
