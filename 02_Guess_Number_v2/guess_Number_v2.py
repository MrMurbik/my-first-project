import random

secret_number = random.randint(1, 20)
attempts = 0

print('Я загадал число от 1 до 20. Попробуй угадать!')

while True:
    user_guess = int(input('Твой вариант: '))
    attempts += 1

    if user_guess == secret_number:
        print(f'Ура! Ты угадал число {secret_number} за {attempts} попыток!')
        break
    elif user_guess < secret_number:
        print('Мое число БОЛЬШЕ')
    else:
        print('Мое число МЕНЬШЕ')

print("Это тестовая ветка! В главной ветке этого текста нет.")
