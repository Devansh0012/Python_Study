dist = int(input("Enter the distance of destination: "))

if dist < 3:
    print("Walk")
    
elif dist <= 15:
    print("Bike")
    
else:
    print("Car")