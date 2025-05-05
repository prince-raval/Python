from datetime import datetime
while True:
    age=int(input("Enter Your age: "))
    today=datetime.now()
    day= today.strftime("%A")
    discount=2
    price=[12,8]
    print(f"Day:-{day}")
    print(f"Time:- {datetime.now()}")
    if age >=18:
        if day=="Wednesday":
            print(f"Discount apply ${discount}")
            print(f"You have to pay {price[0]-2}")
        else:
            print("You have to pay $12 ")
    elif age <18:
        if day=="Wednesday":
            print(f"Discount apply ${discount}")
            print(f"You have to pay {price[1]-2}")
        else:
            print("You have to pay $8 ")
    else:
        print("Please Enter your correct age")
  