def main():
    
    try:
        n  = int(input("Enter a number: "))
    except ValueError:
        print("Enter a valid number!")
        return 0

    print("n:",n)


if __name__ == "__main__":
    main()