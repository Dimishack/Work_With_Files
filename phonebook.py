# Домашнее задание (Урок 8. Работа с файлами):
# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

import os

# Вывод справочника
def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()

# Копирование контакта в другой файл
def copy_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    for contact in list(enumerate(contacts_list)):
        print(f"{contact[0]}: {contact[1].replace("\n", " ")}")
    index = int(input("Выберите номер того контакта, который хотите скопировать: "))
    while index not in range(0, len(contacts_list)):
        print("Некорректный ввод, повторите запрос.")
        index = int(input("Выберите номер того контакта, который хотите скопировать: "))
    with open("contact_copy.txt", 'a', encoding='utf-8') as file:
        file.write(contacts_list[index] + "\n\n")
    print("Контакт успешно скопирован!")

# Поиск
def search_data():
    print("Варианты поиска: \n"
          "1. По фамилии \n"
          "2. По имени\n"
          "3. По отчеству\n"
          "4. По телефону\n"
          "5. По адресу\n")
    command = input("Выберите вариант поиска: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод, повторите запрос.")
        command = input("Выберите вариант поиска: ")

    i_search = int(command) - 1
    search = input("Введите данные для поиска: ").lower()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace('\n', ' ').split(' ')

        if (search in lst_contact[i_search]):
            print("\n" + contact_str)
            check_cont = True
    if not check_cont:
        print("\nТакого контакта не существует.")

# Ввод данных
def input_name():
    return input("Введите имя контакта: ").title()
def input_surname():
    return input("Введите фамилию контакта: ").title()
def input_patronymic():
    return input("Введите отчество контакта: ").title()
def input_phone():
    return input("Введите номер телефона контакта: ").title()
def input_address():
    return input("Введите адрес контакта: ").title()

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"

# Добавить контакт в файл
def add_contact():
    new_contact_str = input_data()
    with open('phonebook.txt', 'a', encoding="utf-8") as file:
        file.write(new_contact_str)

# Интерфейс (начало программы)
def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    command = ""
    os.system("cls")
    while command != "5":
        print("Меню пользователя \n"
              "1. Вывод данных на экран\n"
              "2. Добавить контакт\n"
              "3. Поиск контакта\n"
              "4. Копировать контакт в другой файл\n"
              "5. Выход\n")
        command = input("Выберите пункт меню: ")
        while command not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод, повторите запрос")
            command = input("Выберите пункт меню: ")

        match command:
            case '1':
                print_data()
            case '2':
                add_contact()
            case '3':
                search_data()
            case '4':
                copy_data()
            case '5':
                print("Завершение программы")
        print()

interface()
