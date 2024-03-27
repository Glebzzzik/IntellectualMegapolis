import csv


def open_file(file_name: str):
    # функция для открытия файла
    # file_name - переменная для названия файла
    # data - переменная для чтения файла
    with open(f'{file_name}', encoding='utf-8') as data:
        return list(map(lambda x: x.strip().split('>'), data.readlines()))


def make_file(file_name: str, data_out: list):
    # функция для создания конечного файла
    # file_name - имя файла
    # data_out - данные, которые нужно записать в данный файл
    # data - переменная для чтения файла
    # writer - переменная для записи в файл
    with open(f'{file_name}', 'w', encoding='utf-8') as data:
        writer = csv.writer(data, lineterminator='\n')
        writer.writerows(data_out)


if __name__ == '__main__':
    # основной код
    # data - переменная с данными из файла astronaut_time.txt
    # new_data - переменная с данными для конечного файла
    data = open_file('astronaut_time.txt')
    new_data = [['WatchNumber', 'numberStation', 'cabinNumber', 'timeStop', 'timeNow']]

    for line in data[1:]:
        # обрабатываем и добавляем данные в список для конечного файла
        watchnumber = line[0]
        numberstation = line[1]
        cabinnumber = line[2]
        timestop = line[3]
        count = int(line[4])

        timestop = list(map(int, timestop.split(':')))
        timenow = list(map(str, [(timestop[0] + count) % 24, timestop[1], timestop[2]]))
        timestop = list(map(str, timestop))

        new_data.append([watchnumber, numberstation, cabinnumber, ':'.join(timestop), ':'.join(timenow)])

    make_file('new_time.csv', new_data)

    for i in new_data:
        if i[2] == '98-OYE':
            print(i[-1])
