from data_create import name_data, surname_data, phone_data, adress_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name}; {surname}; {phone}; {adress}\n\n'
                    f'Ваш выбор файла:'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}; {surname}; {phone}; {adress}\n')

    print(f'Данные добавлены в файл {var} ')


def print_data():
    print('Данные из 1-го файла: ')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first_1 = file.readlines()
        data_first_2 = []
        j = 0
        for i in range(len(data_first_1)):
            if data_first_1[i] == '\n':
                data_first_2.append(''.join(data_first_1[j:i]))
                j = i
        data_first_1 = data_first_2
        print(''.join(data_first_1))

        print('Данные из 2-го файла: ')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = list(file.readlines())
        print(''.join(data_second))
    return data_first_1, data_second


def change_line(data_contact, number_contact, var):
    key = input(f'Если меняем данную запись,\n{data_contact[number_contact]}\nто нажмите "enter"')
    number_contact = int(input('Введите номер записи контакта, который надо изменить: ')) - 1

    print(f'Меняем данную запись контакта\n{data_contact[number_contact]}\n')
    if var == 1:
        name = data_contact[number_contact].split('\n')[0]
        surname = data_contact[number_contact].split('\n')[1]
        phone = data_contact[number_contact].split('\n')[2]
        address = data_contact[number_contact].split('\n')[3]
    if var == 2:
        name = data_contact[number_contact].split(';')[0]
        surname = data_contact[number_contact].split(';')[1]
        phone = data_contact[number_contact].split(';')[2]
        address = data_contact[number_contact].split(';')[3]

    key = int(input(f'Какие данные контакта будем менять?\n'
                       f'1 - Имя\n'
                       f'2 - Фамилия\n'
                       f'3 - Номер телефона\n'
                       f'4 - Адрес\n'
                       f'Если определись, то делайте выбор: '))
    if key == 1:
        name = name_data()
    elif key == 2:
        surname = surname_data()
    elif key == 3:
        phone = phone_data()
    elif key == 4:
        address = address_data()

    if var == 1:
        data_first_1 = data_contact[:number_contact] + [f'{name}\n{surname}\n{phone}\n{address}'] + data_contact[number_contact + 1:]
        if number_contact + 1 == len(data_contact):
            data_first_1 = data_contact[:number_contact] + [f'{name}\n{surname}\n{phone}\n{address}\n']
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first_1))
            print('Изменения успешно сохранены в 1-ом файле!')
    else:
        data_second = data_contact[:number_contact] + [f'{name};{surname};{phone};{address}'] + data_contact[number_contact + 1:]
        if number_contact + 1 == len(data_contact):
            data_second = data_contact[:number_contact] + [f'{name};{surname};{phone};{address}\n']
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены во 2-ом файле!')


def change_data():
    print('В каком файле заменить данные?\n')
    data_first_1, data_second = print_data()
    var = int(input('Введите номер файла: '))

    if var == 1: 
        number_contact = int(input('Введите номер записи контакта, который хотите заменить: '))
        number_contact -= 1
        change_line(data_first_1, number_contact, 1)
    else:
        number_contact = int(input('Введите номер записи контакта, который хотите заменить: '))
        number_contact -= 1
        change_line(data_second, number_contact, 2)


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    data_first_1, data_second = print_data()
    var = int(input('Введите номер файла: '))

    while var != 1 and var != 2:
        print('Ой, опять ошибка! Попробуйте еще раз!')
        var = int(input('Введите номер файла: '))

    if var == 1:  
        number_contact = int(input('Введите номер записи контакта, который хотите удалить: '))
        print(f'Удалить данную запись? {data_first_1[number_contact - 1]}')
        del data_first_1[number_contact - 1]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first_1))
        print('Контакт успешно удален из 1-го файла!')
    else:
        number_contact = int(input('Введите номер записи контакта, который хотите удалить: '))
        print(f'Удалить данную запись? {data_second[number_contact - 1]}')
        del data_second[number_contact - 1]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Контакт успешно удален из 2-го файла!')


