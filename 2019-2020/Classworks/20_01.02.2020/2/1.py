from Private.DB import db_config

up_1 = int(input('Entyer up_1: '))
down_1 = int(input('Entyer down_1: '))
up_2 = int(input('Entyer up_2: '))
down_2 = int(input('Entyer down_2: '))

print(f"Addition = {db_config.addition(up_1, down_1, up_2, down_2)}")
print(f"Subtraction = {db_config.subtraction(up_1, down_1, up_2, down_2)}")
print(f"Multiplication = {db_config.multiplication(up_1, down_1, up_2, down_2)}")
print(f"Division = {db_config.division(up_1, down_1, up_2, down_2)}")
