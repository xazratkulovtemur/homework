import random
choices=['rock', 'paper', 'scissors']
computer_point=0
expected_answers=['yes', 'no']
your_point=0
while True: 
    computer_choice=random.choice(choices)  
    your_choice=input("Choose rock, paper, or scissors(or type exit to quit game): ")
    if your_choice=='exit':
        print("Thanks for playing!")
        break
    if your_choice not in choices:
        print("please write your choices in lower cases!")
        continue
    if (computer_choice == 'rock' and your_choice == 'scissors') or (computer_choice=='paper' and your_choice=='rock') or (computer_choice=='scissors' and your_choice=='paper'):
        print("Computer wins!")
        computer_point+=1
    elif (computer_choice==your_choice):
        print("Tie")
    else: 
        print("You win!")
        your_point+=1

    if computer_point>=5:
        computer_point=0
        your_point=0
        print("Computer wins this game!")
        answer=input("Do you want to play again?")
        if answer =='yes':
            continue
        elif answer == 'no':
            break
    if your_point>=5:
        computer_point=0
        your_point=0
        print("You win this game!")
        answer=input("Do you want to play again?")
        if answer =='yes':
            continue
        elif answer == 'no':
            break





