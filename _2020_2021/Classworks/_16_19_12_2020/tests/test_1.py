import pytest
from _2020_2021.Classworks._16_19_12_2020 import _1


def value_sum_test():
    assert isinstance(_1.sum_num_count('0984df'), int)


def value_rand_test():
    assert isinstance(_1.rand(5, 8), int)


def value_count_test():
    assert isinstance(_1.count('0984df', '0'), int)


if __name__ == '__main__':
    value_count_test()
    value_rand_test()
    value_sum_test()
