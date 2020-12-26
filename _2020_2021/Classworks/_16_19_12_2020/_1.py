from random import randint


def sum_num_count(line: str) -> int:
    return sum([int(i) for i in line if i.isdigit()])


def rand(fromm: int, to: int) -> int:
    return randint(fromm, to)


def count(line: str, el: str) -> int:
    return line.count(el)
