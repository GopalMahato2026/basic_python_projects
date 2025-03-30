def main():
    while True:
        user = 1    
        try:    
            user = int(input("Enter a number(7 to exit): "))
            print(f"Number is: {user}")
        except ValueError:
                print("Enter a valid number!")
        except:
            print("\nsomething went worng!")
            return 0    
        if user == 7:
            break
        else:
            try:
                user = int(input("Enter a number(7 to exit): "))
                print(f"Number is: {user}")
            except ValueError:
                print("Enter a valid number!")
            except:
                print("\nsomething went worng!")
                return 0


    print("You broke the loop!")

if __name__ == "__main__":
    main()
