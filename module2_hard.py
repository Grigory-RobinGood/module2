def generate_password(number):
    result = ""

    for i in range(1, 21):  # Нахожу все возможные числа от 1 до 20
        for j in range(i, 21):
            pair_sum = i + j
            if number % pair_sum == 0:  # Проверяю кратность
                if i == j:  # Формирую строку для пароля
                    result += f"{i}{j}"
                else:
                    result += f"{i}{j}"

    return result


num = int(input("Введите число от 3 до 20: "))
if 3 <= num <= 20:
    password = generate_password(num)
    print(f"Пароль для числа {num}: {password}")
else:
    print("Число должно быть от 3 до 20.")
