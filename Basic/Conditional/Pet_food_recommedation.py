pet_species=input("Enter Your Species(i.e Dog,Cat): ").title()
age=int(input("Enter Age: "))
if pet_species=="Dog":
    if age<2:
        food="Puppy Food"
    else:
        food="senior Dog Food"
elif pet_species=="Cat":
    if age >5:
        food="Senior Cat Food"
    else:
        food="Baby Food"
else:
    food = "Normal Food"
print(f"{pet_species} : {food}")