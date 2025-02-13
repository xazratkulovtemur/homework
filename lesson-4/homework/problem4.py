import random
playing =True

tries=0
expected_answers=['yes', 'ok', 'y']
random_number = random.randint(1, 100)

for i in range(10):
    tries+=1
    
    b=int(input("Write a number computer guessed: "))
    if random_number<b:
        print("Too high")
    elif random_number>b:
        print("Too low") 
    
    
    if random_number==b:
        print("You guessed it right!")
        break

    if tries>=10:  
        answer=input("Do you wanna play again? (yes/no)")
        if answer.lower()  in expected_answers:
            playing=True
        else: 
            playing=False

print("Thanks for playing!")
       
    



