class Car:

    def __init__(self, color, count_passenger_seats, is_baby_seat):
        self.color: str = color
        self.count_passenger_seats: int = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f'Car color={self.color}, passenger_seats={self.count_passenger_seats}'


Toyota = Car('blue', 4, 1)
print(Toyota)