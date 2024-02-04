import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        # атрибуты
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.glad = 50
        self.satiety = 10
        self.thirst = 10
        self.mess = 0

    # методы
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        self.job = Job(job_list)

    def eat(self):
        print("0000000000000000000000000000000000000000000")
        if self.home.food < 0:

            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.home.food -= 5

    def drink(self):
        if self.home.water <= 0:
            self.shopping("water")
            self.thirst -= 5
            self.home.water += 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Бензин")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Жраточки+")
            self.money -= 50
            self.home.food += 50
        elif manage == "water":
            print("Водаааа")
            self.money -= 5
            self.home.water += 15
        elif manage == "sweets":
            print("Ура прыщи")
            self.glad += 10
            self.money -= 15
            self.satiety += 2

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.glad -= self.job.glad
        self.satiety -= 15
        self.thirst -= 2

    def chill(self):
        print("Ура отдых")
        self.glad += 20
        self.money -= 10
        self.home.mess += 5

    def clean_home(self):
        self.glad -= 10
        self.home.mess -= 10

    def to_repair(self):
        self.money -= 100
        self.car.strength = 100

    def days_indexes(self, day):
        d = f"Today the {day} of {self.name}'s indexes"
        print(f"{d:=^50}")  # print(f"{d:=^50}") вместо = можно ставить чё хочу
        human_i = f"{self.name}'s indexes"
        # дз надо вывести атрибуты класса Human а именно money,glad,satiety,thirst
        print(f"{human_i:=^50}")
        print(f"{'Home indexes':=^50}")
        # ДЗ 1
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Thirst: {self.thirst}")
        # вывести атрибуты обьекта класса House 3 mess,food,water
        car_i = f"{self.car.brand} car indexes"
        print(f"{car_i:=^50}")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")
        h_i =f" Home indexes"
        print(f"{h_i:=^50}")
        print(f"Mess: {self.home.mess}")  #Дз 2
        print(f"Food: {self.home.food}")
        print(f"Water: {self.home.water}")

    def is_alive(self):
        if self.glad < 0:
            print("в психушку")
            return False
        if self.satiety < 0 or self.thirst < 0:
            print("Пусть земля будет пухом")
            return False
        if self.money < - 100:
            print("Ну всё продадим тебя на органы")
            return False


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Мы не бомжи")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"{self.car.brand} Был куплен")
        if self.job is None:
            self.get_job()
            print(f"I working {self.job.job}, salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety < 20:
            print("Время есть")
            self.eat()
        elif self.thirst > 5:
            print("Время пить")
            self.drink()
        elif self.home.mess > 10:
            print("Срочно убрать")
            self.clean_home()
        elif self.glad < 5:
            print("Время чилить")
            self.chill()
        elif self.money < 5:
            print("Бабки всё нема я почти банкрот")
            self.work()
        elif self.car.strength < 10:
            print("Время отвести кучу метала на ТО")
            self.to_repair()
        elif dice == 1:
            print("Чил")
            self.chill()
        elif dice == 2:
            print("АААА дом=свалка свалка есть убрать")
            self.clean_home()
        elif dice == 3:
            print("Чил")
            self.chill()
        elif dice == 4:
            print("Вкусняшкии ням")
            self.shopping(manage="sweets")



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Автомобиль не едет")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.water = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.glad = job_list[self.job]["glad"]


job_list = {"Python dev": {"salary": 50, "glad": 12},
            "C++ dev": {"salary": 80, "glad": 6},
            "HTML dev": {"salary": 60, "glad": 10},
            "JS dev": {"salary": 75, "glad": 8},
            "Java Dev": {"salary": 100, "glad": 10},
            "Php dev": {"salary": 35, "glad": 2}}

brands_of_car = {"BMW": {"fuel": 100, "strength": 120, "consumption": 14},
                 "Porsche": {"fuel": 170, "strength": 90, "consumption": 99},
                 "Ferrari": {"fuel": 20, "strength": 100, "consumption": 11},
                 "Lamborghini": {"fuel": 60, "strength": 20, "consumption": 1991}}


nick = Human("Nick")
for day in range(1, 100):
    if nick.live(day) == False:
        break