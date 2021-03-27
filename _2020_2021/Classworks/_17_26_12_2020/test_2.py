import pytest


def resource_teardown():
    print("\ndisconnect")


@pytest.fixture(scope='function')  # scope - уровень(для ф-ции/ всех ф-ций в файле)
def resource_setup(request):
    print("\nconnect to conn")
    db = {"Red": 1, "Blue": 2, "Green": 3}

    request.addfinalizer(resource_teardown)  # добавить выполнениие ф-ции после выполнения теста
    return db


def test_red(resource_setup):
    print(resource_setup)  # то что возвращает ф-ция resource_setup
    assert resource_setup["Red"] == 1


@pytest.mark.parametrize("x", [-1, 2])
@pytest.mark.parametrize("y", [-10, 11])  # параметризует аргументы тест-функции
def test_cross_params(x, y):
    print(f"x: {x} y:{y}")  # при нескольких параметризациях будет декартово произведение параметров
    assert True
