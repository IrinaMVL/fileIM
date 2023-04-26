class Car:

    def __init__(self, color, count_passenger_seats, is_baby_seat, is_busy):
        self.color: str = 'blue'
        self.count_passenger_seats: int = 4
        self.is_baby_seat = None
        self.is_busy = False

    def __str__(self):
        return f""


Toyota = Car('Toyota', 'blue', 4, None)
print(Toyota)


