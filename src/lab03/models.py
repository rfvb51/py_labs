from base import Bus
from validate import (
    _validate_has_wifi,
    _validate_has_ac,
    _validate_route_type,
    _validate_has_supervisor,
)

class TouristBus(Bus):
    def __init__(self, route_number, capacity, has_wifi, has_ac, current_speed=0, passenger_count=0):
        super().__init__(route_number, capacity, current_speed, passenger_count)
        self._has_wifi = _validate_has_wifi(has_wifi)
        self._has_ac = _validate_has_ac(has_ac)
        self._route_type = "междугородний"

    @property
    def has_wifi(self):
        return self._has_wifi

    @property
    def has_ac(self):
        return self._has_ac

    @property
    def route_type(self):
        return self._route_type

    def calculate_fare(self):
        base_fare = super().calculate_fare()
        multiplier = 1.5
        if self._has_wifi:
            multiplier += 0.2
        if self._has_ac:
            multiplier += 0.3
        return base_fare * multiplier

    def display_comfort(self):
        comfort_level = "комфорт: "
        if self._has_wifi:
            comfort_level += "Wi-Fi "
        if self._has_ac:
            comfort_level += "кондиционер"
        if not self._has_wifi and not self._has_ac:
            comfort_level += "базовый"
        return comfort_level

    def __str__(self):
        wifi_str = "есть" if self._has_wifi else "нет"
        ac_str = "есть" if self._has_ac else "нет"
        return (super().__str__() + 
                f", тип: туристический, Wi-Fi: {wifi_str}, кондиционер: {ac_str}")

    def __repr__(self):
        return (f"TouristBus({self._route_number}, {self._capacity}, "
                f"{self._has_wifi}, {self._has_ac}, {self._current_speed}, {self._passenger_count})")


class SchoolBus(Bus):
    def __init__(self, route_number, capacity, route_type, has_supervisor, current_speed=0, passenger_count=0):
        super().__init__(route_number, capacity, current_speed, passenger_count)
        self._route_type = _validate_route_type(route_type)
        self._has_supervisor = _validate_has_supervisor(has_supervisor)

    @property
    def route_type(self):
        return self._route_type

    @property
    def has_supervisor(self):
        return self._has_supervisor

    def calculate_fare(self):
        return 0

    def get_safety_info(self):
        if self._has_supervisor:
            return "безопасность: есть сопровождающий"
        return "безопасность: нет сопровождающего"

    def can_transport_children(self):
        return self._has_supervisor

    def __str__(self):
        supervisor_str = "есть" if self._has_supervisor else "нет"
        return (super().__str__() + 
                f", тип: школьный, маршрут: {self._route_type}, сопровождающий: {supervisor_str}")

    def __repr__(self):
        return (f"SchoolBus({self._route_number}, {self._capacity}, "
                f"'{self._route_type}', {self._has_supervisor}, {self._current_speed}, {self._passenger_count})")