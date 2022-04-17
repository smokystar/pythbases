# Number 1

import time
class TrafficLight:
    __color = "White"

    def running(self):
        while True:
            print('trafficlight is red now...')
            time.sleep(5)
            print('trafficlight is yellow now...')
            time.sleep(2)
            print('trafficlight is green now...')
            time.sleep(5)
            print('trafficlight is yellow now...')
            time.sleep(5)
tl = TrafficLight()
tl.running()


# Number 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def profit(self, weight = 35, thickness = 5):
        return f"{self._length} m * {self._width} m * {weight} kg * {thickness} sm = " \
               f"{(self._length * self._width * weight * thickness) / 1000} t"
road_1 = Road(10000, 30)
print(road_1.profit())

# Number 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus" : bonus}
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_full_profit(self):
        return sum(self._income.values())
manager = Position("Petr", "Petrov", "policeman", 40000, 20000)
print(manager.get_full_name())
print(manager.get_full_profit())
print(manager.position)


# Number 4

from random import choice

class Car:
    direction = ["north", "east", "west", "south"]
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'new car: {color} {name}.\nis this car police? {is_police}')

    def go(self):
        print(f'{self.name}: car drive.')
    def stop(self):
        print(f'{self.name}: car stop.')
    def turn(self):
        print(f'{self.name}: car turn {choice(self.direction)}.')
    def show_speed(self):
        return(f'{self.name}: car speed {self.speed}')

class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: car speed: {self.speed}. Speading!' if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: car speed: {self.speed}. Speading!' if self.speed > 40 else super().show_speed()

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super.__init__(speed, color, is_police = True)

police_car = PoliceCar('"ghh"', 'white', 80)
work_car = WorkCar('"ghhdjaga"', 'black', 50)
sport_car = SportCar('"ghhdfjhfhjdga"', 'black', 130)
town_car = TownCar('"asdfghjaga"', 'red', 40)

list_of_cars = [police_car, work_car, sport_car, town_car]
for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()

# Number 5

class Stationery:
    def __init__(self, title="with something that can draw"):
        self.title = title
    def draw(self):
        print(f"Start drawing {self.title}")
class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen")
class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil")
class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker")
stat = Stationery()
pen = Pen("A1")
pencil = Pencil('HB')
marker = Marker('EK')
office_supplies = [stat, pen, pencil, marker]
for i in office_supplies:
    i.draw()