import string
import secrets

symbols = '!@#$%^&*-_'
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + symbols

length = 0
while True:
    try:
        length = int(input('Сколько символов в пароле? (от 4 до 64): '))
    except ValueError:
        print('Ошибка: введите число, например 12.')
        continue
    if length < 4 or length > 64:
        print('Длина должна быть от 4 до 64 символов.')
        continue
    break

password = ''
for i in range(length):
    password += secrets.choice(alphabet)
print(f'Готово! Ваш пароль: {password}')
