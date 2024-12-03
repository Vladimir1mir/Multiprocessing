from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # линейный вызов
    start = datetime.now()
    for name in filenames:
        read_info(name)
    print(datetime.now() - start, '(линейный)')

    # многопроцессный
    start = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start, '(многопроцессный)')
