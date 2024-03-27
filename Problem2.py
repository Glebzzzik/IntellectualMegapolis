def open_file(file_name: str):
    # функция для открытия файла
    # file_name - переменная для названия файла
    # data - переменная для чтения файла
    with open(f'{file_name}', encoding='utf-8') as data:
        return list(map(lambda x: x.strip().split(','), data.readlines()))


def bubble_sort(data: list):
    # функция сортировки пузырьком
    # data - входные данные
    # new_data - отсортированные данные
    new_data = data.copy()[1:]
    for i in range(len(new_data)):
        for j in range(i + 1, len(new_data)):
            if new_data[i][1] > new_data[j][1]:
                new_data[i], new_data[j] = new_data[j], new_data[i]

    return new_data


if __name__ == '__main__':
    # основной код
    # data - считанные данные
    # new_data - отсортированные данные
    data = open_file('new_time.csv')
    new_data = bubble_sort(data)

    for i in range(3):
        numberstation = new_data[i + 1][1]
        cabinnumber = new_data[i + 1][2]
        time_now = new_data[i + 1][-1]
        print(f"На станции {numberstation} в каюте {cabinnumber} восстановлено время. Актуальное время: {time_now}")
