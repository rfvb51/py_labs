import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab02.model import Bus
from lab03.models import TouristBus, SchoolBus
from lab05.collection import AdvancedBusCollection
from lab05.strategies import (
    by_route_number, by_passenger_count, by_load_factor,
    has_passengers, is_tourist_bus, make_capacity_filter,
    double_speed, DiscountLoadStrategy
)

def main():
    print("=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА №5: ФУНКЦИИ КАК АРГУМЕНТЫ")
    print("=" * 70)

    # Создание автобусов
    bus1 = Bus(15, 40)
    bus2 = TouristBus(101, 50, True, True)
    bus3 = SchoolBus(22, 35, "городской", True)
    bus4 = Bus(8, 30)
    bus5 = TouristBus(33, 45, False, True)

    # Подготовка
    for bus in [bus1, bus2, bus3, bus4, bus5]:
        bus.start_route()
    
    bus1.board_passengers(25)
    bus2.board_passengers(40)
    bus3.board_passengers(28)
    bus4.board_passengers(5)
    bus5.board_passengers(35)

    bus1.current_speed = 65
    bus2.current_speed = 55
    bus3.current_speed = 45
    bus4.current_speed = 70
    bus5.current_speed = 50

    collection = AdvancedBusCollection()
    for bus in [bus1, bus2, bus3, bus4, bus5]:
        collection.add(bus)

    # ===== СЦЕНАРИЙ 1: СОРТИРОВКА ТРЕМЯ СТРАТЕГИЯМИ =====
    print("\n1. СОРТИРОВКА ТРЕМЯ СТРАТЕГИЯМИ")
    print("-" * 55)
    
    print("По номеру маршрута:")
    for b in collection.sort_by(by_route_number)._buses:
        print(f"  {b.route_number}: {b.passenger_count} пасс.")
    
    print("\nПо количеству пассажиров:")
    for b in collection.sort_by(by_passenger_count)._buses:
        print(f"  {b.route_number}: {b.passenger_count} пасс.")
    
    print("\nПо загрузке (%):")
    for b in collection.sort_by(by_load_factor)._buses:
        print(f"  {b.route_number}: {b.load_factor()}%")

    # ===== СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ, MAP, LAMBDA, ФАБРИКА =====
    print("\n2. ФИЛЬТРАЦИЯ, MAP, LAMBDA, ФАБРИКА ФУНКЦИЙ")
    print("-" * 55)
    
    print("filter() + lambda - автобусы с пассажирами:")
    for b in filter(lambda x: x.passenger_count > 0, collection._buses):
        print(f"  {b.route_number}: {b.passenger_count} пасс.")
    
    print("\nfilter() по типу (только туристические):")
    for b in filter(is_tourist_bus, collection._buses):
        print(f"  {b.route_number}: {b.passenger_count} пасс.")
    
    print("\nmap() - преобразование в строки:")
    route_strings = list(map(lambda b: f"Автобус №{b.route_number}", collection._buses))
    for s in route_strings:
        print(f"  {s}")
    
    print("\nФабрика функций (фильтр по вместимости >= 40):")
    capacity_filter = make_capacity_filter(40)
    for b in collection.filter_by(capacity_filter)._buses:
        print(f"  {b.route_number}: вместимость {b.capacity}")
    
    print("\nLambda vs именованная функция (сортировка по маршруту):")
    print("  Lambda: " + ", ".join([str(b.route_number) for b in sorted(collection._buses, key=lambda x: x.route_number)]))
    print("  Named:  " + ", ".join([str(b.route_number) for b in collection.sort_by(by_route_number)._buses]))

    # ===== СЦЕНАРИЙ 3: ЦЕПОЧКА ОПЕРАЦИЙ И СТРАТЕГИЯ =====
    print("\n3. ЦЕПОЧКА ОПЕРАЦИЙ И ПАТТЕРН СТРАТЕГИЯ")
    print("-" * 55)
    
    print("Цепочка: filter -> sort -> apply (удвоение скорости):")
    result = (collection
        .filter_by(lambda b: b.passenger_count > 20)
        .sort_by(by_route_number)
        .apply(double_speed))
    for b in result._buses:
        print(f"  {b.route_number}: скорость {b.current_speed:.1f} км/ч, пассажиров {b.passenger_count}")
    
    print("\nCallable-объект как стратегия (DiscountLoadStrategy):")
    strategy = DiscountLoadStrategy()
    for b in collection._buses:
        if b.load_factor() < 30:
            old_speed = b.current_speed
            strategy(b)
            print(f"  {b.route_number}: {old_speed:.1f} -> {b.current_speed:.1f} км/ч")
    
    print("\nЗамена стратегии (разные ключи сортировки):")
    print("  По маршруту:")
    for b in collection.sort_by(by_route_number)._buses[:3]:
        print(f"    {b.route_number}")
    print("  По загрузке:")
    for b in collection.sort_by(by_load_factor)._buses[:3]:
        print(f"    {b.route_number}: {b.load_factor()}%")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()