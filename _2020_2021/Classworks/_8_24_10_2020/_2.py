class Person:
    def __init__(self):
        self.name = None
        self.birth_year = None
        self.id = None

    def insert_data(self, id, name, birth_year, *args, **kwargs):
        self.id = id
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        return f"Name: {self.name}" \
               f"Year of birth: {self.birth_year}" \
               f"ID: {self.id}"


class Passenger(Person):
    def __init__(self):
        super().__init__()
        self.start_location = None
        self.end_location = None
        self.distance = None

    def __repr__(self):
        return f"Start location: {self.start_location}\n"\
               f"End location: {self.end_location}\n" \
               f"Distance: {self.distance}"

    def insert_data(self, id, name, birth_year, *args, **kwargs):
        super().insert_data(id, name, birth_year, *args, **kwargs)
        self.start_location = kwargs.get('start_location')
        self.end_location = kwargs.get('end_location')
        self.distance = kwargs.get('distance')

    def ride_cost(self):
        price = self.price_for_km()
        if price is None:
            raise RuntimeError('Invalid price value: None')
        if self.distance is None:
            raise RuntimeError('Invalid distance value: None')
        return price * self.distance

    @classmethod
    def price_for_km(cls) -> float:
        return 0.55


if __name__ == '__main__':
    data = [
        ('Kyiv', 'Lviv', 234),
        ('A', 'B', 768),
        ('NY', 'LA', 180)
    ]

    passengers = [
        {'name': 'Dima', 'birth_year': 1965},
        {'name': 'Vlad', 'birth_year': 2006},
        {'name': 'Jiso', 'birth_year': 2468}
    ]

    for passenger_id, passenger_data in enumerate(passengers):
        passenger = Passenger()
        print(passenger)
        passenger.insert_data(**passenger_data,
                              start_location=data[passenger_id][0],
                              end_location=data[passenger_id][1],
                              distance=data[passenger_id][2])
        print(passenger)
        print(f"Cost: {passenger.ride_cost()} uah")
