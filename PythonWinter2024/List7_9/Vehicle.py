class Vehicle:
    def __init__(self, manufacturer, fuel_consumption: float):
        self.manufacturer = manufacturer
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"Manufacturer: {self.manufacturer}\nFuel consumption: {self.fuel_consumption}"

    def display(self):
        print(self)

    def cost(self, distance: float, price: float):
        return distance / 100.0 * self.fuel_consumption * price


class Bus(Vehicle):
    def __init__(self, manufacturer, fuel_consumption: float, seats: int):
        super().__init__(manufacturer, fuel_consumption)
        self.seats = seats

    def __str__(self):
        return (f"Manufacturer: {self.manufacturer}\n"
                f"Fuel consumption: {self.fuel_consumption}\n"
                f"Number of seats: {self.seats}")


class Truck(Vehicle):
    def __init__(self, manufacturer, fuel_consumption: float, capacity: int):
        super().__init__(manufacturer, fuel_consumption)
        self.capacity = capacity

    def __str__(self):
        return (f"Manufacturer: {self.manufacturer}\n"
                f"Fuel consumption: {self.fuel_consumption}\n"
                f"Carrying capacity: {self.capacity}")


car = Vehicle("Ford", 7.4)
car.display()
print(car.cost(200, 6))

bus = Bus("Mercedes", 60, 80)
bus.display()
print(bus.cost(100, 6))

truck = Truck("Scania", 18, 18000)
truck.display()
print(truck.cost(1200, 6))
