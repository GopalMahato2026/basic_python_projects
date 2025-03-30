#project is: Number Guessing Game 
"""
steps:
first: I need to generate random number from 1 to 100
then, I will take user's input 
I will need a variable that will store the number of user's guesses
2nd: I set a while loop, this loop will continues its iteration untill 
user's guess is perfect! otherwise i tell them Too high or Too Low! 
3rd: Then I will provide output as the number of guesses user take to guess the number!
"""
from random import randint
def main():
    computer = randint(1,100)
    #error handling if user enter's input is not a number!
    try:
        user = int(input("Enter your guess(1-100): "))
    except ValueError:
        print(f"Enter  a valid Number!")  
        return 0 
    except NameError:
        print("Enter  a valid Number!")  
        return 0   
    guesses = 1
    while computer != user:
        guesses += 1
        if computer < user:
            print("Too High!")
        elif computer > user:
            print("Too Low!")
        #error handling if user enter's input is not a number!
        try:
            user = int(input("Enter your guess(1-100): "))
        except ValueError:
            print(f"Enter  a valid Number!")
            return 0
        except NameError:
            print("Enter  a valid Number!")    
            return 0
    print(f"Its Perfect Guess!\nThe number of guesses: {guesses}")
if __name__ == "__main__":
    main()


