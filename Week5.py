# Assignment 1: Design Your Own Class! 

class Smartphone:
    """
    Represents a smartphone with various attributes and functionalities.
    """
    def __init__(self, brand, model, storage, ram, camera_megapixel):
        """
        Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            storage (int): The internal storage capacity in GB.
            ram (int): The RAM capacity in GB.
            camera_megapixel (float): The resolution of the main camera in megapixels.
        """
        self.brand = brand
        self.model = model
        self.storage = storage
        self.ram = ram
        self.camera_megapixel = camera_megapixel
        self.is_on = False
        self.apps = []

    def power_on(self):
        """Turns the smartphone on."""
        if not self.is_on:
            print(f"{self.brand} {self.model} is powering on...")
            self.is_on = True
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Turns the smartphone off."""
        if self.is_on:
            print(f"{self.brand} {self.model} is powering off...")
            self.is_on = False
        else:
            print(f"{self.brand} {self.model} is already off.")

    def install_app(self, app_name):
        """Installs a new app on the smartphone."""
        if self.is_on:
            if app_name not in self.apps:
                print(f"Installing {app_name} on {self.brand} {self.model}...")
                self.apps.append(app_name)
                print(f"{app_name} installed successfully.")
            else:
                print(f"{app_name} is already installed.")
        else:
            print("Please power on the smartphone first.")

    def uninstall_app(self, app_name):
        """Uninstalls an app from the smartphone."""
        if self.is_on:
            if app_name in self.apps:
                print(f"Uninstalling {app_name} from {self.brand} {self.model}...")
                self.apps.remove(app_name)
                print(f"{app_name} uninstalled successfully.")
            else:
                print(f"{app_name} is not installed.")
        else:
            print("Please power on the smartphone first.")

    def take_photo(self):
        """Simulates taking a photo."""
        if self.is_on:
            print(f"Taking a photo with the {self.camera_megapixel}MP camera on {self.brand} {self.model}...")
        else:
            print("Please power on the smartphone first.")

    def display_info(self):
        """Displays the basic information of the smartphone."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"RAM: {self.ram}GB")
        print(f"Camera: {self.camera_megapixel}MP")
        print(f"Status: {'On' if self.is_on else 'Off'}")
        if self.is_on:
            print(f"Installed Apps: {', '.join(self.apps) or 'None'}")
        print("-" * 20)

# Inheritance Layer: Creating a more advanced smartphone
class GamingSmartphone(Smartphone):
    """
    Represents a gaming-focused smartphone, inheriting from the Smartphone class.
    """
    def __init__(self, brand, model, storage, ram, camera_megapixel, cooling_system, refresh_rate):
        """
        Constructor for GamingSmartphone, adding gaming-specific attributes.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            storage (int): The internal storage capacity in GB.
            ram (int): The RAM capacity in GB.
            camera_megapixel (float): The resolution of the main camera in megapixels.
            cooling_system (str): The type of cooling system.
            refresh_rate (int): The screen refresh rate in Hz.
        """
        super().__init__(brand, model, storage, ram, camera_megapixel)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate

    def start_game(self, game_name):
        """Starts a specific game."""
        if self.is_on:
            print(f"Launching {game_name} on {self.brand} {self.model} with {self.refresh_rate}Hz refresh rate and {self.cooling_system} cooling.")
        else:
            print("Please power on the smartphone first.")

    # Override display_info to include gaming-specific details (Encapsulation/Polymorphism)
    def display_info(self):
        """Displays detailed information about the gaming smartphone."""
        super().display_info()
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate}Hz")
        print("-" * 20)

# Creating instances of the classes
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 8, 50.0)
phone2 = GamingSmartphone("ROG", "Phone 7", 512, 16, 64.0, "Vapor Chamber", 165)

phone1.power_on()
phone1.install_app("WhatsApp")
phone1.install_app("Instagram")
phone1.take_photo()
phone1.display_info()
phone1.power_off()

phone2.power_on()
phone2.install_app("PUBG Mobile")
phone2.start_game("PUBG Mobile")
phone2.display_info()
phone2.power_off()

print("\n" + "=" * 30 + "\n")

# Activity 2: Polymorphism Challenge! 

class Animal:
    def move(self):
        """Generic move method for animals."""
        print("This animal moves.")

class Dog(Animal):
    def move(self):
        print("Running on four legs.")

class Bird(Animal):
    def move(self):
        print("Flying through the air.")

class Fish(Animal):
    def move(self):
        print("Swimming in the water.")

class Vehicle:
    def move(self):
        """Generic move method for vehicles."""
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road. ")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water. ")

# Creating instances of different animals and vehicles
dog = Dog()
bird = Bird()
fish = Fish()
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism by calling the same method on different objects
animals = [dog, bird, fish]
vehicles = [car, plane, boat]

print("Animal Movements:")
for animal in animals:
    animal.move()

print("\nVehicle Movements:")
for vehicle in vehicles:
    vehicle.move()
