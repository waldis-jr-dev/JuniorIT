def to_m(func):
    def wrapper(self):
        if self.value_type == 'km':
            return func(self) * 1000
        if self.value_type == 'm':
            return func(self)
        if self.value_type == 'dm':
            return func(self) * 0.1
        if self.value_type == 'cm':
            return func(self) * 0.01
        if self.value_type == 'mm':
            return func(self) * 0.001
    return wrapper


class Length:
    def __init__(self, value, value_type):
        # value_types: 'mm', 'cm', 'dm', 'm', 'km'
        self.value = value
        self.value_type = value_type

    @to_m
    def get_data(self):
        return self.value


data1 = Length(100, 'cm').get_data() + Length(123, 'cm').get_data() - Length(12, 'km').get_data() * Length(100, 'm').get_data()
data2 = Length(300, 'dm').get_data() + Length(15, 'mm').get_data() - Length(20, 'km').get_data()
print(data1/data2)
