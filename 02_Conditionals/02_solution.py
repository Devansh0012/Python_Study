age = input("Enter your age: ")
age = int(age)

day = input("Enter the day: ")

price = 12 if age >= 18 else 8

if day == "Wednesday" or day == "wednesday":
    price = price - 2
    
print("Your movie ticket price is $", price)
    
