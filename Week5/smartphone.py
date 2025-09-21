# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # Attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    # Methods
    def call(self, number):
        return f"{self.model} is calling {number}..."
    
    def charge(self):
        self.battery = 100
        return f"{self.model} is now fully charged!"
    
    def phone_info(self):
        return f"{self.brand} {self.model} - {self.storage}GB Storage, Battery: {self.battery}%"

# Inheritance example (GamingPhone extends Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    # Overriding a method (Polymorphism)
    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming Edition) - {self.storage}GB, Battery: {self.battery}%, Cooling: {self.cooling_system}"

    # New method for GamingPhone
    def play_game(self, game):
        return f"Playing {game} on {self.model} with {self.cooling_system} cooling system!"

# Testing
phone1 = Smartphone("Samsung", "S22", 128, 75)
phone2 = GamingPhone("Asus", "ROG 6", 256, 50, "Liquid Cooling")

print(phone1.phone_info())
print(phone1.call("+254700123456"))
print(phone2.phone_info())
print(phone2.play_game("PUBG"))
