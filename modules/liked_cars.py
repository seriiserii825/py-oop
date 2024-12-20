# Дядя Гена решил приобрести себе новый автомобиль. Так, он стал рассматривать на
# рынке класс автомобилей с объёмом двигателя 1.6 и чёрным цветом кузова. В
# очередной раз просматривая объявления, дядя Гена обнаружил несколько
# последовательных вариантов автомобилей различных марок и характеристик.
# Помогите дяде Гене внести в класс только те автомобили, которые удовлетворяют его
# интересам. Не забудьте связать каждый новый экземпляр класса автомобилей,
# удовлетворяющих интересам Гены, с моделью данного автомобиля. Выведите
# названия моделей тех автомобилей, которые подходят запросам нашего героя.
from pprint import pprint

results = []

class Car:
    color:str = 'black'
    engine:str = '1.6'
    model: str = ''

with open('data/cars.txt') as file:
    arr = [car[:-1] for car in file.readlines()]
    # pprint(arr)

for index in range(len(arr)):
    car = arr[index].split() 
    if car[2] == Car.engine and car[3] == Car.color:
        liked_car = Car()
        liked_car.model = f"{car[0]} {car[1]}"
        results.append(liked_car)

for car in results:
    pprint(car.__dict__)
