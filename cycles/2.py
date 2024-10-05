saved_pwd = "timurka-pomurka"
pwd = input("Введите пароль для входа: ")
while pwd != saved_pwd:
    pwd = input("Введите пароль для входа: ")
    print("Пароль верный. Вход разрешён.")
