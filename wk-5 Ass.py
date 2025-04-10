# Qn1: Designing My Own Class; Smartphone with Inheritance and Polymorphism

# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def send_message(self, message):
        print(f"Message sent from {self.model}: '{message}'")

    def info(self):
        print(f"Smartphone Info - Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Subclass with additional features
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"{self.model} takes a photo with {self.camera_megapixels}MP camera.")

    # Overriding the info method (Polymorphism)
    def info(self):
        print(f"{self.brand} {self.model} - {self.storage}GB, Camera: {self.camera_megapixels}MP")
phone1 = Smartphone("Nokia", "3310", 16)
phone2 = SmartphoneWithCamera("Apple", "iPhone 14", 256, 12)

phone1.info()
phone1.make_call("123-456-7890")

phone2.info()
phone2.take_photo()
phone2.send_message("Hello from iPhone!")

# Qn2: Polymorphism Challenge – Vehicle Classes 
# Base class
class Vehicle:
    def move(self):
        print("This vehicle moves in a general way.")

# Subclasses with polymorphic behavior

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    print(v.move())
