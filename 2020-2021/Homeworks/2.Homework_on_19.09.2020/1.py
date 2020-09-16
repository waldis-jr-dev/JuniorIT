from typing import Generator, Optional


def lines() -> Generator[Optional[str], Optional[str], None]:
    active_files = {}
    name = 'default'
    resp = yield None
    if resp != '':
        name = resp
    while True:
        while True:
            try:
                with open('files/' + name + '.txt', 'r') as file:
                    data = file.readlines()
                    break
            except FileNotFoundError:
                name = yield 'File not found, try another !'
        if name not in active_files.keys():
            target = range(len(data))
        else:
            target = range(active_files[name] + 1, len(data))
        for number_of_line in target:
            resp = yield data[number_of_line].strip()
            if resp != '':
                active_files[name] = number_of_line
                name = resp
                break
            else:
                continue


if __name__ == '__main__':
    gen = lines()
    next(gen)
    while True:
        answer = input('Name / (enter to continue) : ')
        print(gen.send(answer))
