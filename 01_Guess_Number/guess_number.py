import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    user_guess = int(input('Твой вариант: '))
    attempts += 1

    if user_guess < secret_number:
        print('Мое число БОЛЬШЕ.')

    elif user_guess > secret_number:
        print('Мое число МЕНЬШЕ')

    else:
        print(f'Ура! Ты угадал число {secret_number} за {attempts} попыток!')
        break
