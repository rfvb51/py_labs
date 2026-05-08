"""
Функции-стратегии и callable-объекты для работы с автобусами.
"""

from lab03.models import TouristBus, SchoolBus

# ===== СТРАТЕГИИ СОРТИРОВКИ (ЗАДАНИЕ 3) =====

def by_route_number(bus):
    """Сортировка по номеру маршрута (по возрастанию)"""
    return bus.route_number

def by_passenger_count(bus):
    """Сортировка по количеству пассажиров (по возрастанию)"""
    return bus.passenger_count

def by_load_factor(bus):
    """Сортировка по загрузке в процентах (по возрастанию)"""
    return bus.load_factor()

# ===== ФУНКЦИИ-ФИЛЬТРЫ (ЗАДАНИЕ 3) =====

def has_passengers(bus):
    """Фильтр: автобусы с пассажирами"""
    return bus.passenger_count > 0

def is_tourist_bus(bus):
    """Фильтр: только туристические автобусы"""
    return isinstance(bus, TouristBus)

# ===== ФАБРИКА ФУНКЦИЙ (ЗАДАНИЕ 4) =====

def make_capacity_filter(min_capacity):
    """
    Фабрика функций - создаёт фильтр по минимальной вместимости.
    
    Args:
        min_capacity: минимальная вместимость
    
    Returns:
        функция-фильтр, принимающая автобус и возвращающая bool
    """
    def filter_fn(bus):
        return bus.capacity >= min_capacity
    return filter_fn

# ===== ФУНКЦИИ ДЛЯ APPLY (ЗАДАНИЕ 5) =====

def double_speed(bus):
    """Удваивает скорость автобуса, но не более 120 км/ч"""
    from copy import deepcopy
    new_bus = deepcopy(bus)
    new_bus.current_speed = min(new_bus.current_speed * 2, 120)
    return new_bus

# ===== CALLABLE-ОБЪЕКТЫ (ПАТТЕРН СТРАТЕГИЯ) (ЗАДАНИЕ 5) =====

class DiscountLoadStrategy:
    """
    Стратегия снижения скорости для малозагруженных автобусов.
    Если загрузка < 30%, скорость уменьшается на 20%.
    """
    
    def __call__(self, bus):
        if bus.load_factor() < 30:
            bus.current_speed = max(bus.current_speed * 0.8, 1)
        return bus