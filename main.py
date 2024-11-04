# def generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# for i in generator():
#     print(i)
# --------------------------------------------------
# def my_range(start, stop, step=1):
#     while start < stop:
#         start += step
#         yield start
#
#
# print(list(my_range(1, 9)))
# 1------------------------------
# def my_range(start, stop, step=1):
#     while start < stop:
#         start += step
#         yield start
#
#
# print(list(my_range(1, 9)))
# 2------------------------------
# def my_range(start, stop):
#     juft = []
#     while start < stop:
#         if start % 2 == 0:
#             juft.append(start)
#         yield juft
#
#
# print(list(my_range(1, 9)))
# ---------------------Tuple-------------------------
# 1-----------
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(tup)
# 2-----------
# students = ("Safobek", "Azizbek", "Abdulbosit", "Sherdorbek")
# print(students[2])
# 3-----------
# tup1 = ("safobek", ("knfwnfjwnl"))
# print(tup1)
# 4-----------
# students = ("Safobek", "Azizbek", "Abdulbosit", "Sherdorbek")
# print(len(students))
# 5-----------
# tup1 = ("Safobek", "Azizbek", "Abdulbosit", "Sherdorbek")
# tup2 = ("Safobek2", "Azizbek2", "Abdulbosit2", "Sherdorbek2")
# tup3 = ("Safobek3", "Azizbek3", "Abdulbosit3", "Sherdorbek3")
# tup4 = ("Safobek4", "Azizbek4", "Abdulbosit4", "Sherdorbek4")
# tup5 = ("Safobek5", "Azizbek5", "Abdulbosit5", "Sherdorbek5")
# tupall = tup1+tup2+tup3+tup4+tup5
# l = list(tupall)
# l.sort()
# print(l)
# 6-----------
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for num in tup:
#     print(num * 2)
# 7-----------

