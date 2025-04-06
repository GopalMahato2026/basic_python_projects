## Rock Paper Scissors Game!
## i will assign rock as 1 paper as 0 and scissor as -1, and then i will generate random choice/number
## of these three choices ; user will enter r as rock, p as paper, s as scissor (for this i will need a dictionary )
## that will have keys and values like like this {"r":1,"p":0,"s":-1} So computer and user both will choose these numebrs(1,0,-1) 
## then, I need do this thing i will show who choose what! for this to action i will need another dictionary
## like this {1:"rock", 0:"paper", -1:"scissor"}
## then, I will determine who wins according to game's rule(rock beats scissor, paper beats rock, scissor beats paper)
## one more feature computer and user have to choose how many round then want to play!
from random import choice
def main():
    print("Rock Paper Scissor Game")
    computer = choice([1,0,-1])
    user_list = ["r","p","s"]
    user = input("Enter your choice(r,p,s): ").lower()
    if user not in user_list:
        print(f"Invaild Choice: {user}")
    user_dict = {"r":1,"p":0,"s":-1}
    main_user = user_dict[user]  #main_user have 1,0 or -1 value
    show_dict = {1:"rock",0:"paper",-1:"scissor"} 
    print(f"Computer Choose: {show_dict[computer]}\nYou choose: {show_dict[main_user]}")

    #lets determining the winner
    if computer == main_user:
        print(f"Its a Draw!")
    elif (computer == 1 and main_user == 0) or (computer == 0 and main_user == -1) or (computer == -1 and main_user == 1):
        print("You Win!")
    else:
        print("You Lose!")
            





if __name__ == "__main__":
    main()