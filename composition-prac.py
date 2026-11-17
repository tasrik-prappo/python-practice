class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower


class Wheel:
    def __init__(self, wheel_size: int):
        self.wheel_size = wheel_size


class Car:
    def __init__(self, name: str, model: str, horse_power: int, wheel_size: int):
        self.name = name
        self.model = model
        # Composition: Car creates and owns its Engine and Wheel objects internally
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def display_car(self) -> str:
        return (
            f"{self.name} {self.model} "
            f"{self.engine.horsepower}hp "
            f"{self.wheels[0].wheel_size}in"
        )


car1 = Car(name="Ford", model="Mustang", horse_power=761, wheel_size=18)
print(car1.display_car())