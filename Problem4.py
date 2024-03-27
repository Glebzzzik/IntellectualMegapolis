def open_file(file_name: str):
    # функция для открытия файла
    # file_name - переменная для названия файла
    # data - переменная для чтения файла
    with open(f'{file_name}', encoding='utf-8') as data:
        return list(map(lambda x: x.strip().split(','), data.readlines()))


if __name__ == '__main__':
    # основной код
    # data - переменная для считывания данных
    # from_00_to_12 - переменная для станций, которые остановились в промежутке от 0 до 12
    # from_12_to_00 - переменная для станций, которые остановились в промежутке от 12 до 0
    data = open_file('new_time.csv')
    from_00_to_12 = []
    from_12_to_00 = []
    for i in data[1:]:
        x = list(map(int, i[-2].split(':')))

        if 0 <= x[0] <= 11 or (x[0] == 12 and x[2] == 0):
            from_00_to_12.append(i)
        else:
            from_12_to_00.append(i)

    print(
        f"{len(from_00_to_12)} станций остановилось с период с 00.00 до 12.00.\n{len(from_12_to_00)} станций остановилось с период с 12.01 до 23.59.")
