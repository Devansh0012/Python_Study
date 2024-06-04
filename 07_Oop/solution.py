class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Toyota
print(my_car.model)  # Corolla

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)  # Tata
print(my_new_car.model)  # Safari