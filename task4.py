#4 Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
#*Пример:*
 #45 -> 101101
#- 3 -> 11
#- 2 -> 10
number_dec = int(input("Введите десятичное число: "))
number_bin = '' 
while number_dec > 0:
    number_bin = str(number_dec % 2) + number_bin
    number_dec = number_dec // 2
print(number_bin)