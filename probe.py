# greetings = ['hello', 'hi', 'hey', 'hola']
# name= greetings[0][1]
# p= greetings[1][1]
# e=greetings[2][1]
# t=greetings[3][1]
# bla= name + p + e + t
# g=[letter  for letter in bla]
# print(g)
# kf=[greetin[1] for greetin in greetings]
# print(kf)
#
# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# gl= [bb  for bb in digits if bb % 2 ==0]
# print(max(gl))
#
# greetinhs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# letter_list = []
# for greeting  in greetinhs:
#     if greeting % 2 ==0:
#      letter_list.append(greeting)
# print(letter_list)
#
# digitps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_numbers = [digit for digit in digitps if digit % 2 == 1]
# print(odd_numbers)
#
# x=1
#
#
# for bbl in  range(100):
#
#         co=0
#         text=""
#         while co <= bbl:
#
#             text += "Pasha Gul "
#             co += 1
#             print(text)
# x=1
# while x==1:
#
#     for bbl in range(1,11):
#
#         print("ph " * bbl)

# sm=[[1,3,6,2],[234,564,1423],["text", False,True],[55,1234]]
# for bbl in sm:
#     for sl in bbl:
#
#         print(sl)
# print(sm[2][2])
#
# def cat_voice (name= "Lera"):
#     print("Meow " + name + "Meow")
#
# cat_voice()
#
# def dog_voice (name):
#     '''
#
#     :param name: its your name
#     :return: None kdfkjkf
#     '''
#     print("Gaph \t" + name + "Gaph")
#
# dog_voice("lucia")
# help(dog_voice)

# def voice (who):
#     if "cat" in who:
#         return print("Meow")
#     elif "dog" in who:
#         return print("Gaph")
#     else:
#         return print("Who kto ?")
#
# voice("cal,")
#
# def ll(a,b):
#     ss_d=
#     letter_list = []
# for greeting  in ss:
#     if greeting % 2 ==0:
#      letter_list.append(greeting)
# print(letter_list)
#
# ll(2, 4)
#
#
# def is_cat_here(*args):
#     args_in_lower_case = [str(argument).lower() for argument in list(args)]
#     if 'cat' in args_in_lower_case:
#         return True
#     else:
#         return False
#
#
# print(is_cat_here("ss", "name", "Cat"))
#
#
# def item(item, *args):
#     print(item)
#     print(args)
#
#
# print(item(5, 3, 2, "name", 6, "bbl"))

#
# my_car = "bam"
# kkl=.3123
# print(id(my_car))
# print(type(kkl))
# print(my_car.replace("a","g"))

# go=[2,53,657,324,4]
# go.extend([312,13,42,66])
# go.insert(0,"bll")
# del go[-1]
# go.remove(657)
#
#
# print(go)
#
# name = list(range(3, 10, 2))
# name.append("vl")
# name.extend([123, 56, 63])
# del name[2:4]
# name.insert(-1, 444)
# name.remove("vl")
# name.sort()
# print(name)
# #
# my={12312,24,45324,234,243,24,565,677,58,4}
# bbl={23,24,23,234,3453,4567,67,4523,4}
#
# print(my | bbl)
# print(my & bbl)
# # print(my - bbl)
# pari = ("ss", "sa")
# mi = ("as", "dd", "sa")
# m_set = set(pari)
# mi_set = set(mi)
# print(m_set | mi_set)
# print(m_set & mi_set)
#
# date_birthiday = 1
# if date_birthiday < 0:
#     print("Ok")
#     pass
# elif date_birthiday == 1:
#
#     name = "Lucia"
#     print("hello {}".format(name))
# else:
#     print("balla")
from pprint import pprint
#
# ------------ While

# f1, f2 = 1,1
# print(f1)
# while f2 < 1000:
#     print(f2)
#     f1,f2 = f2, f1+f2


# #
# my_pets = ['lion', 'dog', 'skunk', 'hamster', 'cat', 'monkey']
# i = -1
# while i < len(my_pets):
#     i += 1
#     if i == 2:
#         continue
#     pet = my_pets[i]
#
#     print('Проверяем ', pet)
#     if pet == 'cat':
#         print('Ура, кот найден!')
#         break
# print('дотвиданя!')
#
#
# f1, f2, count = 0, 1, 0
# while f2 < 10000:
#     count += 1
#     if count > 27:
#         print('Итераций больше чем 27. Прерываюсь.')
#         break
#     f1, f2 = f2, f1 + f2
#     if f2 < 1000:
#         continue
#     print(f2)
# else:
#     print('Было', count, 'итераций')
#
# xz = 0
# if xz < 19:
#     pass
# print("ss")
#
# my_animals = ["cat","elephant","tiger",'dog',"birds"]
#
# for zoo in enumerate(my_animals):
#     if zoo == "dog":
#         print("fuu")
#         continue
#     print("proverka {}".format(zoo))
#     if zoo == "birds":
#
#         print("Ok good")
#         break
#         if zoo == "cat":
#             pass
#
# print("nashli")
#
#
# for i in my_animals:
#     for char in i:
#         print(char)
#     print(i)


import simple_draw

simple_draw.resolution = (1200, 600)

point = simple_draw.get_point(50, 50)

simple_draw.line(start_point=50, end_point=350, width=1)
vector_1.draw()

simple_draw.pause()