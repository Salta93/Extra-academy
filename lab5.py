class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_string(self):
        print(self.__str__())

class Driver(Person):
    def __init__(self, first_name, last_name, driving_experience):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_experience = driving_experience

    def __str__(self):
        return f'{self.first_name} {self.last_name}, Стаж вождения: {self.driving_experience}'

class Engine:
    def __init__(self, power, manufacturer):
        self.power = power
        self.manufacturer = manufacturer

    def __str__(self):
        return f'{self.power} л.с., {self.manufacturer}'

class Car:
    def __init__(self, model, car_class, weight, driver: Driver, engine: Engine):
        self.model = model
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def to_string(self):
        print(self.__str__())


    def __str__(self):
        car_info = f"Марка: {self.model}\n"
        car_info += f"Класс: {self.car_class}\n"
        car_info += f"Вес: {self.weight}\n"
        car_info += f"Водитель: {self.driver}\n"
        car_info += f"Мотор: {self.engine}\n"
        return car_info

#грузовик
class Lorry(Car):
    def __init__(self, model, car_class, weight, driver, engine, load_capacity):
        super().__init__(model, car_class, weight, driver, engine)
        self.load_capacity = load_capacity

    def __str__(self):
        car_info = f"Информация о грузовике:\nМарка: {self.model}, Класс {self.car_class}, Вес: {self.weight}, Водитель: {self.driver}, Мотор: {self.engine}\nГрузоподъемность: {self.load_capacity} кг\n "
        return car_info

#спорткар
class SportCar(Car):
    def __init__(self, model, car_class, weight, driver, engine, max_speed):
        super().__init__(model, car_class, weight, driver, engine)
        self.max_speed = max_speed

    def  __str__(self):
        car_info = f"Информация о спорткаре:\nМарка: {self.model}, Класс: {self.car_class}, Вес: {self.weight}, Водитель: {self.driver}, Мотор: {self.engine} \nПредельная скорость: {self.max_speed} км/ч\n"
        return car_info

toyota_engine = Engine(200, 'Toyota')
volvo_engine = Engine(300, 'Volvo')
ferrari_engine = Engine(400, 'Ferrari')

driver1 = Driver('Иван', 'Иванов', 5)
driver2 = Driver('Петр', 'Петров', 10)
driver3 = Driver('Анна', 'Сидорова', 3)

car = Car('Toyota Camry', 'Седан', 1500, driver1, toyota_engine)
lorry = Lorry('Volvo FH', 'Грузовик', 8000, driver2, volvo_engine, 5000)
sport_car = SportCar('Ferrari 488', 'Спорткар', 1500, driver3, ferrari_engine, 300)

car.to_string()
lorry.to_string()
sport_car.to_string()
