# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# План:
# 1. Создание файла
# 2. Добавление новой записи
#     * забрать ввод пользователя
#     * открытие файла на дозапись
#     * записать в файл
# 3. Вывод на экран
#     * открыть файл на чтение
#     * считывание данных
#     * вывод на экран
# 4. Поиск контакта
#     * выбрать вариант поиска
#     * забрать ввод пользователя
#     * открыть файл на чтение
#     * считать данные
#     * осуществить поиск
#     * вывод результата на экран
# 5. Создание интерфейса


# ДОБАВИТЬ КОНТАКТ
def add_contact():
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'a', encoding='utf-8') as file:
        name = input('Введите ФИО или псевдоним: ').title()
        number = input('Введите номер телефона: ')
        file.write(name + ' ' + number + '\n')
    if __name__ == '__main__':
        interface()


# ВЫВЕСТИ ВСЕ КОНТАКТЫ
def print_contacts():
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'r', encoding='utf-8') as file:
    # for line in file_name:
    #     print(line)
        print(file.read())
    if __name__ == '__main__':
        interface()


# ПОИСК КОНТАКТА
def search_contact():
    temp = input('Введите имя или номер для поиска контакта: ').lower()
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if temp in line.lower():
                print(line, end='')
    if __name__ == '__main__':
        interface()


# ИЗМЕНИТЬ КОНТАКТ
def change_contact():
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'r', encoding='utf-8') as file:
        all_contacts = dict(enumerate([line for line in file.read().rstrip().split('\n')], 1))
        for i, contact in all_contacts.items():
            print(f"{i}. {contact}")
    contact_chn = check_input_num('Введите номер контакта: ')
    while not 1 <= int(contact_chn) <= len(all_contacts):
        print('Такого контакта нет!')
        contact_chn = check_input_num('Введите номер контакта: ')
    new_name = input('Введите новое ФИО или псевдоним: ').title()
    new_number = input('Введите новый номер телефона: ')
    all_contacts[int(contact_chn)] = new_name + ' ' + new_number
    # print(all_contacts[int(contact_chn)])
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'w', encoding='utf-8') as file:
        for value in all_contacts.values():
            file.write(value + '\n')

    if __name__ == '__main__':
        interface()


# УДАЛИТЬ КОНТАКТ
def delete_contact():
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'r', encoding='utf-8') as file:
        all_contacts = dict(enumerate([i for i in file.read().rstrip().split('\n')], 1))
        for i, contact in all_contacts.items():
            print(f"{i}. {contact}")
    del_contact = check_input_num('Введите номер контакта: ')
    while not 1 <= int(del_contact) <= len(all_contacts):
        print('Такого контакта нет!')
        del_contact = check_input_num('Введите номер контакта: ')
    del all_contacts[int(del_contact)]
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'w', encoding='utf-8') as file:
        for value in all_contacts.values():
            file.write(value + '\n')

    if __name__ == '__main__':
        interface()


# Копировать контакт в другой файл
def copy_contact():
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'r', encoding='utf-8') as file:
        contacts = dict(enumerate([i for i in file.read().strip().split('\n')], 1))
        for nn, value in contacts.items():
            print(f'{nn}. {value}')
        contact_for_copy = check_input_num('Выберите контакт для копирования: ')
        while not 1 <= int(contact_for_copy) <= len(contacts):
            print('Под таким номером нет контакта!!!')
            contact_for_copy = check_input_num('Выберите контакт для копирования: ')
        
        with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/new_phonebook.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(contacts[int(contact_for_copy)] + '\n')
        print('\n' + 'Контакт скопирован :)')

    if __name__ == '__main__':
        interface()


# ПРОВЕРКА НА ЧИСЛО
def check_input_num(message):
    input_text = input(message)
    while not input_text.isdigit():
        print('Некорректные данные!')
        input_text = input(message)
    return input_text


# MAIN
def interface():
    with open('c:/programist/Study/Python/seminars/seminar_8_work_with_files/phonebook.txt', 'a') as phonebook:
        pass
    print(
        '\nВарианты действий:\n'
        '1. Добавить контакт\n'
        '2. Вывод списка контактов\n'
        '3. Поиск контактов\n'
        '4. Изменить контакт\n'
        '5. Удалить контакт\n'
        '6. Копировать контакт в другой файл\n'
        '7. Выход\n'
    )

    user_input = check_input_num('Выберите вариант: ')
    
    while not 1 <= int(user_input) <= 7:
        print('Такого варианта нет!')
        user_input = check_input_num('Выберите вариант: ')

    print()
    if user_input == '1':
        add_contact()
    elif user_input == '2':
        print_contacts()
    elif user_input == '3':
        search_contact()
    elif user_input == '4':
        change_contact()
    elif user_input == '5':
        delete_contact()
    elif user_input == '6':
        copy_contact()
    else:
        print('До скорой встречи!')


if __name__ == '__main__':
    interface()