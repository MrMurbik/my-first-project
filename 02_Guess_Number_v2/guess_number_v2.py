import random

secret_number = random.randint(1, 20)
attempts = 0

print('Я загадал число от 1 до 20. Попробуй угадать!')

while True:
    try:
        user_guess = int(input("Твой вариант: "))
    except ValueError:
        print("Ошибка! Нужно ввести число цифрами. Попробуй еще раз.")
        continue

    attempts += 1

    if user_guess == secret_number:
        print(f'Ура! Ты угадал число {secret_number} за {attempts} попыток!')
        break
    elif user_guess < secret_number:
        print('Мое число БОЛЬШЕ')
    else:
        print('Мое число МЕНЬШЕ')
