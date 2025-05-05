distance=int(input("Please Enter Distance: "))
if distance<3:
    print("Please walk")
elif distance<16:
    print("Please Take a Bike")
elif distance>15:
    print("Please Take Car")
else:
    print("Please Eneter Valid input")
