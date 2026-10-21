class Engine():

    def __init__(self,horsepower: int):
        self.horsepower = horsepower

def Wheel():

    def __init__(self,wheelsize: int):
        self.wheelsize = wheelsize

def Car():

    def __init__(self,name,model,horse_power,wheel_size):
        self.name = name
        self.model = model
        self.horse_power = Engine(horse_power)
        self.wheel_size = [Wheel(wheel_size for i in range(4))]

    def display_car(self):
        return f"{self.name}  {self.model}  {self.horse_power}  {self.wheel_size[1]}"

    
w1, w2, w3, w4 = Wheel(18), Wheel(18), Wheel(18), Wheel(18)
car1 = Car(name="Ford",model="Mustang",horse_power=761,wheel_size=[w1,w2,w3,w4])
print(car1.display_car())