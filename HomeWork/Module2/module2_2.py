first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
third = int(input('Ведите третье число:'))

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
