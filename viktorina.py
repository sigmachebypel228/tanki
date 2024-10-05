from random import randint

student = input('Представьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности 1 - 5: '))
except:
    level = 1
    print('Установлен первый уровень сложности.')
if level < 1 or level > 5:
    level = 1
    print('Установлен первый уровень сложности.')
print(f'Хорошо,{student}, проверь свои знания по географии .')
questions =[
    ('Столица Франции?','Париж'),
    ('Самая длинная река в мире?:','Амазонка'),
    ('Самая высокая гора на Земле?','Эверест'),
    ('Какой океан самый большой?','Тихий Океан'),
    ('Какой континент самый маленький?','Австралия'),
]
points = 0
for i in range(5):
    question = questions[randint(0,len(questions)-1)]
    print(f'{student},{question[0]}')
    answer = input()

    if answer.lower() == question[1].lower():
        points+=1
        print('Правильно!')
    else:
        print(f'Неправильно! Правильный ответ {question[1]} .')
if points == 5:
    print(f'Удивительно , {student}, ты настоящий знаток географии!')
elif points >= 3:
    print(f'Молодец, {student}.Ты справился на {points} правильных ответов.')
else:
    print(f'Плохо, {student}.Всего  правильных {points} ответов !')