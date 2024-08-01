my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
a = my_list[index]
while index < len(my_list) and my_list[index] >= 0:
    print(my_list[index])
    index += 1
    if my_list[index] == 0:
        index += 1
print('Вроде правильно!')