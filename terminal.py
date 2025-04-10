#i get a idea from my mind that is a linux terminal
##when user enter su or root or sudo i will ask them passwords
user = input("Enter your password: ").lower()
name = input("Enter your name: ").lower()
with open("password.txt",'w') as pass_:
    pass_.write(user) 
    print(f"Added {user} successfully!") 

user_input = input("Enter your user_name: ").lower()
user_pass = input("Enter your password: ").lower()
if user_input == name and user_pass == user:
    print("bash")
    print("-----------------")
    print(f"Wellcome back {user_input}")

    root_list = ["su","sudo","root"]
    root_user = input(f"{user}@fedora: ")
    if root_user in root_list:
        if root_user.lower() == "su"  or "sudo":
            print("What you want to do buddy!")
            print(f"root@fedora# ")
    else:
        print(f"'{root_user}' not develop yet!")     


elif user_input == name or user_pass ==user:
    print(f"Invalid username or password!")
else:
    print("something went worng!")    



