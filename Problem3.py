def open_file(file_name: str):
    # функция для открытия файла
    # file_name - переменная для названия файла
    # data - переменная для чтения файла
    with open(f'{file_name}', encoding='utf-8') as data:
        return list(map(lambda x: x.strip().split(','), data.readlines()))


def find_cabin(cayutnumber: str, data):
    # функция для поиска кабины
    # data - данные, в которых ищем
    # cayutnumber - номер нужной кабины

    for i in data:
        if i[2] == cayutnumber:
            print(i[2])
            return f"В каюте {i[2]} восстановлено время (время остановки: {i[-2]}).\nАктуальное время: {i[-1]}"
    return 'В этой каюте все хорошо'


if __name__ == '__main__':
    # основной код
    # data - переменная с данными из файла astronaut_time.txt
    # cayutnumber - переменная для считывания кабины
    data = open_file('new_time.csv')
    cayutnumber = ''
    while True:

        if cayutnumber == 'none':
            break
        else:
            if cayutnumber != '':
                print(find_cabin(cayutnumber, data))

            cayutnumber = input("Введите номер каюты: ")

