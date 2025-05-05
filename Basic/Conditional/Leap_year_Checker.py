year=int(input("Enter Year: "))
if (year%400 ==0) or (year%4 ==0 and year%100 != 0):
    y="Leap Year"
else:
    y="not Leap Year"
print(f"Year: {y}")
