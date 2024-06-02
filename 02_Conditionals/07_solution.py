order_size = input("Enter the size of your coffee: ")

extra_shots = input("Do you want extra shots? (y/n): ")
extra_shots = extra_shots.lower()
if extra_shots == "y":
    extra_shots = True
else:
    extra_shots = False
    
if order_size == "small":
    print("You ordered a small coffee.")
    if extra_shots:
        print("You ordered extra shots.")
    else:
        print("You did not order extra shots.")
elif order_size == "medium":
    print("You ordered a medium coffee.")
    if extra_shots:
        print("You ordered extra shots.")
    else:
        print("You did not order extra shots.")
elif order_size == "large":
    print("You ordered a large coffee.")
    if extra_shots:
        print("You ordered extra shots.")
    else:
        print("You did not order extra shots.")
else:
    print("We do not have that size.")