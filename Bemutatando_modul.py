import requests

while True:
    print('1. Elérhető e az oldal?')
    print('2. Az oldal html kódja')
    print('3. Kontent típus')
    while True:
        try:
            ans = int(input())
            break
        except:
            print('rossz adat')
    if ans == 1:
        response = requests.get('https://w3schools.com/python/demopage.htm')
        if response.status_code == 200:
            print('Awailable!')
        elif response.status_code == 404:
            print('Not Found.')
        else:
            print('what?')
    elif ans == 2:

        x = requests.get('https://w3schools.com/python/demopage.htm')
        print(x.text)
    elif ans == 3:
        response = requests.get('https://w3schools.com/python/demopage.htm')
        print(response.headers['Content-Type'])
    else:
        print('rossz adat')
