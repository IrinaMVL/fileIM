class Car:

    def __init__(self, color, count_passenger_seats, is_baby_seat, is_busy):
        self.color = color.str()
        self.count_passenger_seats = count_passenger_seats.int()
        self.is_baby_seat = None
        self.is_busy = False


Toyota = Car()


