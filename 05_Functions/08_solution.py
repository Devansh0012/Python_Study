def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(name = "shaktiman", power = "lazer")
print_kwargs(name = "shaktiman", power = "lazer", city = "Fursatganj")
print_kwargs(name = "shaktiman", power = "lazer", city = "Fursatganj", enemy = "Kilvish")
