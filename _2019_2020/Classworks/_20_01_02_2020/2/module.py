import mod


def addition(up_1, down_1, up_2, down_2):
    answ_up = up_1 * down_2 + up_2 * down_1
    answ_down = down_1 * down_2
    return mod.f(answ_up, answ_down)


def subtraction(up_1, down_1, up_2, down_2):
    answ_up = up_1 * down_2 - up_2 * down_1
    answ_down = down_1 * down_2
    return mod.f(answ_up, answ_down)


def multiplication(up_1, down_1, up_2, down_2):
    answ_up = up_1 * up_2
    answ_down = down_1 * down_2
    return mod.f(answ_up, answ_down)


def division(up_1, down_1, up_2, down_2):
    answ_up = up_1 * down_2
    answ_down = down_1 * up_2
    return mod.f(answ_up, answ_down)
