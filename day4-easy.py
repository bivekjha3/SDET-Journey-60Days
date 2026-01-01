# This is the Blueprint (Class)
class Car:
    
    # This is the "Birth" function. 
    # It runs automatically when a new Car is born.
    # 'self' means "MYSELF" (The car being born).
    def __init__(self, brand_name, color):
        self.brand = brand_name
        self.color = color
        print(f"Factory: A new {self.color} {self.brand} is ready!")

    # This is an Action (Method)
    def drive(self):
        print(f"Vroom! The {self.brand} is moving.")
    # --- Main Road (Execution) ---

# 1. Build the first car (Object 1)
my_car = Car("Hyundai Creta", "White")
# Result: The Factory prints "A new White Hyundai Creta is ready!"

# 2. Build the second car (Object 2)
brother_car = Car("Suzuki Swift", "Red")
# Result: The Factory prints "A new Red Suzuki Swift is ready!"

# 3. Drive them
my_car.drive()      # Prints: Vroom! The Hyundai Creta is moving.
brother_car.drive() # Prints: Vroom! The Suzuki Swift is moving.