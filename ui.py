from logger import input_data, print_data, put_data, delete_data

def interfece():
    print("Добрый день! вы попали на специальный бот справочник от Алексея Синягина \n 1 - запись данных \n 2 - вывод данных \n 3 - удаление данных \n 4 - редактирование данных")
    command = int(input())

    while command < 1 or command > 4:
        print("Неправильный ввод")
        command = int(input('Введите число '))
    
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        put_data()


