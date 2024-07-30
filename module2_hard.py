def generate_password(number):
    result = ""

    for i in range(1, 21):              # Нахожу все возможные числа от 1 до 20
        for j in range(i + 1, 21):
            pair_sum = i + j            # Нахожу сумму чисел
            if number % pair_sum == 0:  # Проверяю кратность
                result += f"{i}{j}"     # Вывожу результат в строку

    return result


num = int(input("Введите число от 3 до 20: "))      # Ввводим число
if 3 <= num <= 20:                                  # Проверяем диапазон чисел
    password = generate_password(num)               # Запускаем функцию
    print(f"Пароль для числа {num}: {password}")    # Выводим результат
else:
    print("Число должно быть от 3 до 20.")          # Ошибка при выходе за диапазон
