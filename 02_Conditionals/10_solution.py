species = input("Enter your pet's species: ")
age = int(input("Enter your pet's age: "))

if species == "dog":
    if age < 2:
        print("Puppy")
    elif age < 6:
        print("Adult")
    else:
        print("Senior")
        
elif species == "cat":
    if age < 2:
        print("Kitten")
    elif age < 6:
        print("Adult")
    else:
        print("Senior")
        
else:
    print("Unknown species")