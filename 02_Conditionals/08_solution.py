password = input("Enter your password: ")

if len(password) < 6:
    print("Weak")
    
elif len(password) < 10:
    print("Medium")
    
else:
    print("Strong")