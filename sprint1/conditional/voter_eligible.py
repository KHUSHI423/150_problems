if __name__ == "__main__":
    age = int(input("Enter your age: "))
    citizen = int(input("Are you a citizen? (1 for Yes, 0 for No): "))
    disqualified = int(input("Are you disqualified from voting? (1 for Yes, 0 for No): "))
    if age >= 18 and citizen == 1 and disqualified == 0:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")