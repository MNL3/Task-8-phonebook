from logger import input_data, print_data, delete_data, change_data

def interface():
    print('Добрый день! Это бот-помощник.\n'
          'Что Вы хотите сделать? \n'
          '1 - Записать данные\n'
          '2 - Удалить данные\n'
          '3 - Изменить данные\n'
          '4 - Вывести данные\n')

    command = int(input('Ваш выбор: '))

    while command < 1 or command > 4:
        command = int(input('Ошибка! Попробуйте ещё раз! Итак, Ваш выбор: '))

    if command == 1:
        input_data()
    elif command == 2:
        delete_data()
    elif command == 3:
        change_data()
    elif command == 4:
        print_data()

interface()
  