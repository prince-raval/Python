Coffee_Name=input("Please Enter Coffee Name: ").strip().lower()
order_size=input("Enter Order Size(i.e: Large\Medium\Small): ").lower().strip()
extra_shot=input("Please Enter(Yes/No): ").strip().lower()

Coffee_Name=Coffee_Name.capitalize()
order_size=order_size.capitalize()

if extra_shot=="yes":
    full_order=f"{order_size} {Coffee_Name} with an Extra Shot"
elif extra_shot=="no":
    full_order=f"{order_size} {Coffee_Name} without an Extra Shot"
else:
    full_order=f"{order_size} {Coffee_Name}"

print(f"Order summary: {full_order}")

