# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# from itertools import count
# new_f = open("new_file.txt", "w")
#
# a=[]
# text = str()
# for i in count(1):
#     text=input('Введите текст: ')
#     if text == "":
#         break
#     a.append(text+"\n")
# print(a)
# new_f.writelines(a)
# new_f.close()



# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

# print("Задача 2")
# file_obj = open("lesson5_task2", "r", encoding="utf-8")
#
# list=file_obj.readlines()
# a = len(list)
# print(f"Количество строк:{a}")
# print(list)
# i=0
# for el in list:
#     i=i+1
#     print(f"{i} строка - количество слов {len(el.split())}")
#
#
# file_obj.close()



# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# пример списка
#
# ФИО           Оклад
# Иванов И.И.     15000
# Сидорова О.И.   21000
# Воронин С.Д.    19000
# Петров В.В.     25000
# Гусев В.М.      22000
# Созинова Т.И.   18000
# Лебедева И.М.   20000
# Ветров В.В.     31000
# Белова В.Д.     21000


#
# print("Задача 3")
# salary=open("Salary",encoding="utf=8") # открываем файл
#        # salary=open(r"C:\Users\Dmitry\PycharmProjects\Lessons\Salary",encoding="utf=8") # открываем файл
# list_fio=salary.readlines() # читаем построчно и создаем объект по типу List
# print(list_fio) # печатаем для проверки что получилось (получился List с данными string)
#
# i=1 # обозначаем начало отсчета для цикла. Пропускаем шапку.
# a=len(list_fio) # выясняем длинну списка
# while i<a:
#     if int(list_fio[i].split()[2]) < 20000: # разбиваем текст по пробелу. Получили 3 элемента. По 3 му элементу (зарплата) ставим фильтр менее 20000
#         print(f"{list_fio[i].split()[0]} {list_fio[i].split()[1]} - {int(list_fio[i].split()[2])}") # печать
#     i=i+1
#
# salary.close

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

# print("Задача 4")
#      # obj_eng=open(r"C:\Users\Dmitry\PycharmProjects\Lessons\Eng_letters",encoding="utf-8")
# obj_eng=open("Eng_letters",encoding="utf-8")
# eng_list=obj_eng.readlines() # создаем объект списком, прочитав построчно файл. При этом, элементы string
# rus_dict={1:"Один",2:"Два",3:"Три",4:"Четыре",5:"Пять",6:"Шесть",7:"Семь",8:"Восемь",9:"Девять",0:"Ноль"}
# print(eng_list)
#
# eng_list_end=[]
# for i in range(0,len(eng_list)):
#     eng_list_end.append(f"{int(eng_list[i].split()[2])} - {rus_dict.get(int(eng_list[i].split()[2]))}\n")# делаем split и по 3 элементу (ключ) вытаскиваем из словаря русс значение
#
# print(eng_list_end)
#
# rus_letter=open("Rus_letters.txt","w",encoding="utf-8") # открываем/создаем новый файл для записи русс букв
# rus_letter.writelines(eng_list_end) # записываем построчно в файл
# obj_eng.close # закрываем файл
# rus_letter.close() # закрываем файл

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# sum_file=open("Sum_file.txt","w")
# a=[1,2,3,5,6,4,3,2,7,8,9,23]
# b=[]
# i=0
# sum=0
# while i < len(a):
#     b.append(f" {a[i]}")
#     sum=sum+a[i]
#     i=i+1
# b.append(f" сумма ={sum}")
# sum_file.writelines(b)
# print(sum)
# sum_file.close()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
# print("Задача 6")
#       #pred_file=open(r"C:\Users\Dmitry\PycharmProjects\Lessons\Predmety",encoding="utf-8")
# pred_file=open("Predmety",encoding="utf-8")
# pred_list=pred_file.readlines()
# print(pred_list)
# split_list=[]
# for el in pred_list:
#     split_list.append(el.split())
# print(split_list)
#
# # очистим данные от скобок
# c="("
# i=0
# j=0
# split_list_final=[]
#
# for i in split_list:# проходимся по основному списку
#     d=[]
#     for j in i: # проходимся по символам в элементах основного списка
#           if j!="-":
#             b=[]
#             for x in j: # пройдемся по буквам
#                 if x == "(":
#                     break
#                 b.append(x) # добавляем нужные символы в списки 3го уровня
#
#             d.append("".join(b)) #объединим символы в слова и добавим в список второго уровня
#             #print(d)
#     split_list_final.append(d) #добавим списки слов в список первого уровня
#
# print(split_list_final)
# # создаем финальный словарь
# my_dict={}
# key_list=[]
# value_list=[]
# for i in split_list_final:
#     a=0
#     for j in i:
#         if j == i[0]:
#             key_list.append(j)
#         else:
#             a=a+(int(j))
#         # print(key_list)
#         # print(a)
#     value_list.append(a)
# print(key_list)
# print(value_list)
# my_dict=dict(zip(key_list,value_list))
#
# print(my_dict)
#
# pred_file.close()


#
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

# print("Задача 7")
# firms_info=open("Firms_7",encoding="utf-8")
# firms_list=firms_info.readlines()
# print(firms_list)
#
# firms_list_split=[]
# for line in firms_list:
#     firms_list_split.append(line.split())
# print(firms_list_split)
#
# name=[]
# status=[]
# revenue=[]
# costs=[]
# for line in firms_list_split:
#
#     for el in line:
#         if el == line[0]:
#             name.append(el)
#         elif el == line[1]:
#             status.append(el)
#         elif el == line[2]:
#             revenue.append(int(el))
#         elif el == line[3]:
#             costs.append(int(el))
#
# profit=[]
# for rev,cos in zip(revenue,costs):
#     p=rev-cos
#     profit.append(p)
#
# final_dict=dict(zip(name,profit))
#
# print(name)
# print(status)
# print(revenue)
# print(costs)
# print(profit)
#
# print(final_dict)


#
# firms_info.close