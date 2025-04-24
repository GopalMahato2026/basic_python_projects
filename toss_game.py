# lets make head and tails game
from random import choice
total = 0
win = 0
lose = 0
while True:
    total += 1
    user = input("Do you want to toss(y/n): ").lower()
    if user == 'n':
        print("You exited!")
        break
    try:    
        user_loop = int(input("How many times you want to toss?: "))
    except:
        print("something went worng!")    
    for times in range(user_loop):
        toss = choice([1,0])
        total = user_loop
        if user == 'y': 
            user_input = int(input("Enter your choice(1-head,0-tails): "))
            if user_input == toss:
                print("You Win The TOSS!")
                win += 1
            elif user_input != toss:
                print("You Lose THE TOSS!")
                lose += 1
    else:
        print("You exited the program!")
        print(f"Total Plays: {total}\nTotal Wins: {win}\nTotal Loses: {lose}")
        break
              