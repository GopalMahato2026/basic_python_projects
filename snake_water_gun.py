#snake water gun game this game is very much similer to rock_paper_scissor
## i assign snake as 1 water as 0 and gun as -1
## game rules: snake beats water, water beats gun and gun beats snake
from random import choice
def main():
    print("Snake Water Gun Game")
    computer = choice([1,0,-1])
    user_list = ["s","w","g"]
    user = input("Enter your choice(s, w, g): ").lower()
    if user not in user_list:
        print(f"Invaild Choice: {user}")
    user_dict = {"s":1, "w":0, "g":-1}
    main_user = user_dict[user]  #main_user have 1,0 or -1 value
    show_dict = {1:"snake",0:"water",-1:"gun"} 
    print(f"Computer Choose: {show_dict[computer]}\nYou choose: {show_dict[main_user]}")

    #lets determining the winner
    #game rules: snake(1) beats water(0), water(0) beats gun(-1) and gun(-1) beats snake(-1)
    if computer == main_user:
        print(f"Its a Draw!")
    elif computer == 1 and main_user == 0:
        print("You lose!")
    elif computer == 1 and main_user == -1:
        print("You Win!")
    elif computer == 0 and main_user == 1: #0 == gun 1 == snake 
        print("You Win!")
    elif computer == 0 and main_user == -1:
        print("You lose!")                        
    elif computer == -1 and main_user == 0:
        print("You Win!")
    elif computer == -1 and main_user == 1:
        print("You lose!")


if __name__ == "__main__":
    main()