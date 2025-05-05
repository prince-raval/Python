while True:
    age=int(input("Enter Your age: "))
    if age < 13:
        print("Opps! You are Child")
    elif age <20:
        print("You are Teenagers")
    elif age <=59:
        print("you are Adult")
    else:
        print("You are Senior")