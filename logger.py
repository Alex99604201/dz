from data_create import name_data, surname_data, phone_data, adress_data

def input_data():
   name = name_data()
   surname = surname_data()
   phone = phone_data()
   adress = adress_data()
   var = int(input(f"В каком форрмате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберете вариант: "))

   while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

   if var == 1:
       with open('data_telephone.csv', 'a', encoding='utf-8') as f:
           f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
   elif var == 2:
       with open('data_telephone2.csv', 'a', encoding='utf-8') as f:
           f.write(f"{name};{surname};{phone};{adress}\n\n")

def print_data():
    print('Вывожу данные из 1го файла: \n')
    with open('data_telephone.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из 2го файла: \n')
    with open('data_telephone2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def change_line(dataFile, numberRow, numberFile):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow]}?\nВведите ответ: ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: '))
        numberRow -= 1

    print(f"Меняем данную запись\n{dataFile[numberRow]}")
    if numberFile == 1:
        name = dataFile[numberRow].split('\n')[0]
        surname = dataFile[numberRow].split('\n')[1]
        phone = dataFile[numberRow].split('\n')[2]
        address = dataFile[numberRow].split('\n')[3]
    if numberFile == 2:
        name = dataFile[numberRow].split(';')[0]
        surname = dataFile[numberRow].split(';')[1]
        phone = dataFile[numberRow].split(';')[2]
        address = dataFile[numberRow].split(';')[3]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Имя\n"
                       f"2. Фамилия\n"
                       f"3. Номер телефона\n"
                       f"4. Адрес\n"
                       f"Введите ответ: "))
    while answer < 1 or answer > 4:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 4")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Имя\n"
                           f"2. Фамилия\n"
                           f"3. Номер телефона\n"
                           f"4. Адрес\n"
                           f"Введите ответ: "))
    if answer == 1:
        name = name_data()
    elif answer == 2:
        surname = surname_data()
    elif answer == 3:
        phone = phone_data()
    elif answer == 4:
        address = adress_data()

    if numberFile == 1:
        data_first = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}'] + \
                     dataFile[numberRow + 1:]
        if numberRow + 1 == len(dataFile):
            data_first = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}\n']
        with open('data_telephone.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first))
        print('Изменения успешно сохранены!')
    else:
        data_second = dataFile[:numberRow] + [f'{name};{surname};{phone};{address}'] + \
                      dataFile[numberRow + 1:]
        if numberRow + 1 == len(dataFile):
            data_second = dataFile[:numberRow] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                         dataFile[numberRow + 1:]
        with open('data_telephone2.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')


def put_data():
    print('Из какого файла Вы хотите изменить данные?')
    with open('data_telephone.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
    with open('data_telephone2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неправильный ввод')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        change_line(data_first_list, number_journal, 1)
    else:
        print("Какую именно запись по счету Вы хотите изменить?")
        number_journal = int(input('Введите номер записи: '))
        number_journal -= 1
        change_line(data_second, number_journal, 2)


def delete_data():
    print('Из какого файла Вы хотите удалить данные?')
    with open('data_telephone.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
    with open('data_telephone2.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()

    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неправильный ввод')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:  
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        while number_journal > len(data_first_list) or number_journal < len(data_first_list):
           print('Неправильный ввод')
           number_file = int(input('Введите номер файла: '))
        print(f'Удалить данную запись\n{data_first_list[number_journal - 1]}')
        data_first_list = data_first_list[:number_journal - 1] + data_first_list[number_journal + 1:]
        with open('data_telephone.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_first_list))
        print('Изменения успешно сохранены!')
    else:
        print("Какую именно запись по счету Вы хотите удалить?")
        number_journal = int(input('Введите номер записи: '))
        while number_journal > len(data_first_list) or number_journal < len(data_first_list):
           print('Неправильный ввод')
           number_file = int(input('Введите номер файла: '))
        print(f'Удалить данную запись\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal -1] + data_second[number_journal + 1:]
        with open('data_telephone2.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_second))
        print('Изменения успешно сохранены!')