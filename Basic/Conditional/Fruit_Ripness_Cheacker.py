while True:
    fruit=input("Please Enter Valid fruit Name: ")
    coulour_of_fruit=input("Please Enter Colour Of Fruit(Yellow/Green/Brown): ")
# yellow="Ripe"
# green="Unrip"
# brown="Overrip"
    if coulour_of_fruit.lower()=="yellow":
        print(f"The fruit is Ripe")
    elif coulour_of_fruit=="green":
        print(f"The fruit is Unripe")
    elif coulour_of_fruit=="brown":
        print(f"The fruit is Overripe")
    else:
        print("please enter Valid Colour")
