from lab02.model import Bus
from lab04.interfaces import Printable, Comparable


class TouristBus(Bus, Printable, Comparable):
    def __init__(self, route_number, capacity, current_speed, passenger_count, guide_name, tour_price):
        super().__init__(route_number, capacity, current_speed, passenger_count)
        self._guide_name = guide_name
        self._tour_price = tour_price

    def calculate_income(self):
        return self.passenger_count * self._tour_price

    def to_string(self):
        return f"[TouristBus] Гид: {self._guide_name}, пассажиры: {self.passenger_count}, доход: {self.calculate_income()}"

    def compare_to(self, other):
        if not isinstance(other, TouristBus):
            raise TypeError("Можно сравнивать только TouristBus")
        return self.calculate_income() - other.calculate_income()

    def __str__(self):
        return f"[Туристический] {super().__str__()} | гид: {self._guide_name}, цена тура: {self._tour_price} руб."


class SchoolBus(Bus, Printable):
    def __init__(self, route_number, capacity, current_speed, passenger_count, school_name, has_supervisor):
        super().__init__(route_number, capacity, current_speed, passenger_count)
        self._school_name = school_name
        self._has_supervisor = has_supervisor

    def calculate_income(self):
        return 0

    def to_string(self):
        supervisor = "есть" if self._has_supervisor else "нет"
        return f"[SchoolBus] Школа: {self._school_name}, сопровождающий: {supervisor}, пассажиры: {self.passenger_count}"

    def __str__(self):
        supervisor = "есть" if self._has_supervisor else "нет"
        return f"[Школьный] {super().__str__()} | школа: {self._school_name}, сопровождающий: {supervisor}"