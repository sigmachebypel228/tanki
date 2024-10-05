user_input = ""
while user_input.lower() != "exit":
    user_input = input("Введите команду (или 'exit' для выхода): ")
    print(f"Вы ввели: {user_input}")

saved_pwd = "timurka-pomurka"
pwd = input("Введите пароль для входа: ")
while pwd != saved_pwd:
    pwd = input("Введите пароль для входа: ")
    print("Пароль верный. Вход разрешён.")

fruitsList = ["Манго", "Яблоко", "Апельсинка", "Гуава"]
for chr in "THis is THe TEst sTRinG":
    if chr.islower():
        print(chr.upper())
    else:
        print(chr)

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
for i in collection:
    l = n*i
    print(l)

for i in range(1, 6):
    for j in range(1, 6):
        print(i, j)

my_list = [1, 2, 3, 4, 5]
total = 0
for element in my_list:
    total += element
print(f"Сумма элементов списка: {total}")