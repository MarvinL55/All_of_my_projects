myPets = ["Sophie", "Pooka", "Fat-tail"]
print("Enter pet Name:")
name = input()

if name not in myPets:
    print("I do not have a pet named " + name + " listed")
else:
    print(name + " is my pet ")
