# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и
# т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]
my_list= [2, 3, 4, 5, 6]
print(my_list)
import math
middle= (math.ceil((len(my_list))/2))
for i in range(0, middle, 1):
    my_list[i]= my_list[i] * my_list[(len(my_list)-1)-i]
del my_list[middle:len(my_list)]
print(my_list)
