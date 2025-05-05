while True:
    marks=int(input("Enter Your Marks: "))
    Grade=""
    if marks>=90:
        print(f"Your total marks: {marks} with Grade 'A'")
    elif marks >=80:
        print(f"Your total marks: {marks} with Grade 'B'")
    elif marks >=70:
        print(f"Your total marks: {marks} with Grade 'C'")
    elif marks>=60:
        print(f"Your total marks: {marks} with Grade 'D'")
    else:
        print("sorry! You Failed")
