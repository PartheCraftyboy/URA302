def is_within_range(num):
    return 100 <= num <= 1000 or num == 2000

# Take input from the user
def main():
    try:
        user_input = int(input("Enter a number: "))
        result = is_within_range(user_input)
        if result:
            print("The number is within the range of 100 to 1000 or exactly 2000.")
        else:
            print("The number is not within the range of 100 to 1000 or exactly 2000.")
    except ValueError:
        print("enter correct value, try again")
        main()

main()