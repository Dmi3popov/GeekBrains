# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
# — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

# print("Задача 1")
# class TrafficLight:
#     # атрибуты класса
#     __color = "red"
#     # методы класса
#     def running(self):
#         import time
#         print(self.__color)
#         time.sleep (7)
#         color="yellow"
#         print(color)
#         time.sleep(2)
#         color ="green"
#         print(color)
#         time.sleep(8)
# a=TrafficLight()
# print(a)
# print(type(a))
# a.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# print("Задача 2")
# class Road:
#     def __init__(self, lenght, width, height):
#         self._lenght=lenght
#         self._width=width
#         self._height=height
#         self.asphalt()
#     def asphalt(self):
#         const=25/1000
#         a=self._lenght*self._width*self._height*const
#         return(a)
#
# b=Road(250,10,10)
# print(b.asphalt())
# c=Road(20,5000,5)
# print(c.asphalt())


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на
# базе класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

# print("Задача 3")
# class Worker:
#     # атрибуты класса
#     worker_wage={"wage":50000,"bonus":10000}
#     # конструктор
#     def __init__(self, name,surname,position):
#         self.name=name
#         self.surname=surname
#         self.position=position
#         self._income()
#     # методы класса
#     def _income(self):
#         a = self.worker_wage.get("wage")+self.worker_wage.get("bonus")
#         return(a)
# class Position(Worker):
#     def get_full_name(self):
#         print(f"{self.name} {self.surname}")
#     def get_total_income(self):
#         print(f"доход {self._income()}")
#
#
# b=Position("Ivan","Petrov", "operator")
# print(b.get_full_name())
# print(b.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

# print("Задача 4")
# class Car:
#     def __init__(self,speed,color,name,is_police):
#         self.speed=speed
#         self.color=color
#         self.name=name
#         self.is_police=False
#     def go(self):
#         print(f"Машина {self.name} поехала!")
#     def stop(self):
#         print(f"Машина {self.name} остановилась!")
#     def turn(self):
#         a=input("Поверните направо или налеао: ")
#         print(f" Машина {self.name} повернула {a}")
#     def show_speed(self):
#         print(f"Скорость {self.name} составляет {self.speed}")
#
# class TownCar(Car):
#     size = 1
#     def show_speed(self):
#         if self.speed>60:
#             print(f"Скорость {self.name} равна {self.speed} и превышает допустимую скорость 60 ")
#         else:
#             print(f"Скорость {self.name} составляет {self.speed}")
#
# class WorkCar(Car):
#     size = 3
#     def show_speed(self):
#         if self.speed>40:
#             print(f"Скорость {self.name} равна {self.speed} и превышает допустимую скорость 40 ")
#         else:
#             print(f"Скорость {self.name} составляет {self.speed}")
#
# car=Car(40,"red","Mustang",False)
# print(car.name)
# car.go()
# car.stop()
# car.show_speed()
# car.turn()
#
# car1=TownCar(65,"white","Opel",False)
# print(car1.name)
# car1.go()
# car1.stop()
# car1.show_speed()
# # car1.turn()
#
# car2=WorkCar(55,"grey","MB",False)
# print(car2.name)
# car2.go()
# car2.stop()
# car2.show_speed()
# # car2.turn()

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
# атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# print("Задача 5")
#
# class Stationery:
#     def __init__(self,title):
#         self.title=title
#     def draw(self):
#         print("Запуск отрисовки")
# class Pen(Stationery):
#     def draw(self):
#         self.title="Pen"
#         print("Запуск отрисовки ручкой.")
# class Pencil(Stationery):
#     def draw(self):
#         #self.title="Pencil"
#         print("Запуск отрисовки карандашом.")
#
# class Handle(Stationery):
#     def draw(self):
#         #self.title="Handle"
#         print("Запуск отрисовки маркером.")
#
# a=Stationery("pencil")
# a.draw()
# print(a.title)
#
# b=Pen("Pen")
# b.draw()
# print(b.title)
#
# c=Handle("Handle")
# c.draw()
# print(c.title)