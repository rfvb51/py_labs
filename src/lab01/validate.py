# ЛР-1, транспорт - автобус (валидация)

def _validate_route_number(value):
    if not isinstance(value, int):
        raise TypeError("номер маршрута должен быть целым числом")
    if value <= 0:
        raise ValueError("номер маршрута должен быть положительным")
    if value < 1 or value > 999:
        raise ValueError("номер маршрута должен быть от 1 до 999")
    return value

def _validate_capacity(value):
    if not isinstance(value, int):
        raise TypeError("вместимость должна быть целым числом")
    if value <= 0:
        raise ValueError("вместимость должна быть положительной")
    if value > 50:
        raise ValueError("вместимость не может превышать 50")
    return value

def _validate_speed(value, max_speed):
    if not isinstance(value, (int, float)):
        raise TypeError("скорость должна быть числом")
    if value < 0:
        raise ValueError("скорость не может быть отрицательной")
    if value > max_speed:
        raise ValueError(f"скорость не может превышать {max_speed}")
    return float(value)

def _validate_passenger_count(value, capacity):
    if not isinstance(value, int):
        raise TypeError("количество пассажиров должно быть целым числом")
    if value < 0:
        raise ValueError("количество пассажиров не может быть отрицательным")
    if value > capacity:
        raise ValueError("количество пассажиров не может превышать вместимость")
    return value