def greet(name="User"):
        return f"Hello, {name}!"
    
name = input("Enter your name: ")
print(greet(name))