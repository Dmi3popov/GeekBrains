# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
# class Matrix:
#     def __init__(self,my_matrix):
#         self.my_matrix=my_matrix
#     def __str__(self):
#         for row in self.my_matrix:
#             print(row)
#         return(str(self.my_matrix))
#     def __add__(self,other):
#         result_matrix=[]
#         for i,j in zip(self.my_matrix,other.my_matrix):
#             z=[]
#             for x,y in zip(i, j):
#                 z.append(x+y)
#             result_matrix.append(z)
#
#         return Matrix(result_matrix)
#
# a=Matrix([[1,2,3],[2,3,4],[3,4,5]])
# b=Matrix([[1,1,1],[2,2,2],[3,3,3]])
# c=a+b
# print(a)
# print(b)
# print(c)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self,param):
        self.param=param

    @abstractmethod
    def calcul(self):
        pass

class Suit(Clothes):

    def calcul(self):
        return self.param*2+0.3

a=Suit(1.8)
print(a.calcul)

class Coat(Clothes):

    def calcul(self):
        return self.param/6.5+0.5

a=Coat(44)
print(a.calcul)





# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

# class Cell:
#     def __init__(self,num):
#         self.num=num # количество ячеек клетки
#
#     def __add__(self,other):
#         return Cell(self.num+other.num)
#     def __str__(self):
#         return (str(self.num))
#     def __truediv__(self,other):
#         #return Cell(self.num/other.num)
#         return Cell((self.num+other.num)/self.param)
#
#     def make_order(self,param):
#         self.param=param # количество ячеек в ряду
#         x=1
#         while x<(self.num/self.param):
#             z=[]
#             if param>0:
#                 for i in range(0,param):
#                     z.append("*")
#                 z.append("\n")
#             x=x+1
#             print(z)
# a=Cell(7)
# b=Cell(3)
# c=a+b
# c.make_order(3)
# print(c)
