password=input("Enter your password: ")
if len(password)<6:
    passwd=f"Weak"
elif len(password)<11:
    passwd=f"Medium"
else:
    passwd=f"Strong"
print(f"Password Strength: {passwd}")