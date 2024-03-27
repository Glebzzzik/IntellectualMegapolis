def open_file(file_name: str):
    # функция для открытия файла
    # file_name - переменная для названия файла
    # data - переменная для чтения файла
    with open(f'{file_name}', encoding='utf-8') as data:
        return list(map(lambda x: x.strip().split(','), data.readlines()))


if __name__ == '__main__':
    data = open_file('new_time.csv')
    hashes = dict()
    data = list(map(lambda x: [x[0], x[1], hash(x[2]), x[3], x[4]], data))
    data = sorted(data, key=lambda x: x[2])
    for i in data:
        hashes[i[2]] = [i[0], i[1], i[3], i[4]]

    for i, j in enumerate(hashes, start=1):
        if i <= 10:
            print(', '.join(hashes[j]))
