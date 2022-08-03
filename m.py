users = {
    'Admin':{
        'name':'admin',
        'phone':'996555444333',
        'balance':500000,
        'password':'12312321'
    },
    'Argen':{
        'name':'Argen',
        'phone':'999580780',
        'balance':5000,
        'password':'12312321'
    }
}
key = None
while True:
    print('Здраствуйте уважаемый клиент!')
    m = int(input('''
    1 Заарегистрироваться 
    2 Авторизоваться 
    3 Перевод баланса
    4 Список пользователей 
    5 Информатция 
    6 Изменить логин
    7 Изменить пароль
    8 Выход из банка
    >>> '''))
    if m == 1:
        if key is None:
            login = input('введите логин ')
            name = input('введите полное ваше имя ')
            phone = int(input('введите ваш номер +996'))
            password = input('Придумайте пароль ')
            password1 = input('Подтвердите пароль ')
            while password != password1 and len(password) < 8:
                password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
                password1 = input('Повторите пароль ')
            else:
                users.update({
                    login :{
                        'name':name,
                        'phone':phone,
                        'balance':1000,
                        'password':password
                    }
                })
                print('Регистратция успешна')
                key = login
    elif m == 2:    
        if key is None:
            print('Добро пожаловать в авторизатцию ')
            login = input('Введите логин ')
            password = input('введите пароль ')
            if login in users:
                if password == users[login]['password']:
                    print('Вы авторизовались ')
                    key = login
                else:[print('Не верный пароль')]
            else:[print('Нет такого пользователя ')]
        else:[print('Вы уже авторизованы ')]
    elif m == 3:
        if users is not None:
            loginP = input('Введите имя получателя ')
            summa = int(input('введите сумму перевода '))
            if loginP in users:
                if summa <= users[key]['balance']:
                    users[key]['balance'] -= summa
                    users[loginP]['balance']+= summa
                    print('Перевод успешен')
                else:[print('У вас не достаточно денег')]
            else:[print('такого пользователя нет')]
        else:[print('вы не авторизованы')]
    elif m == 4:
        if key is not None:
            print(users)
    elif m == 5:
        if key is not None:[print(f'''
            Логин: {users["Admin"]}
            Имя: {users["Admin"]['name']}
            Номер телефона: {users["Admin"]['phone']}
            Баланс: {users["Admin"]['balance']}
            \n''')]
        else:[print('вы не авторизованы')]
    elif m == 6:
        if key is not None:
            print(f'\nВаш login: {login}\n')
            new_login = input('Введите новый логин: ')
            login = new_login
            print(f'Логин успешно обновлён на {login}')
        else:[print('вы не авторизованы')]
    elif m == 7:
        if key is not None:
            print(f'\nВаш пароль: {users["Admin"]["password"]}\n')
            password = input('Введите текуший пароль: ')
            if password == users[key]['password']:
                password = input('Введите новый пароль: ')
                password1 = input('Подтвердите новый пароль: ')
                while password != password1 and len(password) < 8:
                    password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
                    password1 = input('Подтвердите новый пароль ')
                else:[users.update({
                        login :{
                            'name':name,
                            'phone':phone,
                            'balance':1000,
                            'password':password
                        }
                    })]
            else:[print('Извините пароль не верный')]
        else:[print('вы не авторизованы')]
    elif m == 8:
        print('Приходите ещё ')
        break
    else:[print('Брат такой команды нет')]
    