from base import Bus
from models import TouristBus, SchoolBus

def main():
    print("=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА №3: НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ")
    print("=" * 70)

    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ И МЕТОДЫ БАЗОВОГО/ДОЧЕРНИХ КЛАССОВ")
    print("-" * 50)

    bus_base = Bus(15, 40)
    tourist_bus = TouristBus(101, 50, True, True)
    school_bus = SchoolBus(22, 35, "городской", True)

    print("Базовый автобус:", bus_base)
    print("Туристический:", tourist_bus)
    print("Школьный:", school_bus)

    print("\nНовые атрибуты дочерних классов:")
    print(f"  Туристический: Wi-Fi={tourist_bus.has_wifi}, кондиционер={tourist_bus.has_ac}, тип={tourist_bus.route_type}")
    print(f"  Школьный: тип маршрута={school_bus.route_type}, сопровождающий={school_bus.has_supervisor}")

    print("\nНовые методы дочерних классов:")
    print(f"  {tourist_bus.display_comfort()}")
    print(f"  {school_bus.get_safety_info()}")

    print("\n2. ПОЛИМОРФИЗМ: МЕТОД calculate_fare()")
    print("-" * 50)

    for bus in [bus_base, tourist_bus, school_bus]:
        bus.start_route()
        bus.board_passengers(30)
        print(f"  Автобус №{bus.route_number}: стоимость проезда = {bus.calculate_fare():.2f} руб.")

    print("\n3. КОЛЛЕКЦИЯ РАЗНЫХ ТИПОВ И ФИЛЬТРАЦИЯ")
    print("-" * 50)

    fleet = [bus_base, tourist_bus, school_bus]

    print("Все автобусы в коллекции:")
    for i, bus in enumerate(fleet, 1):
        print(f"  {i}. {bus}")

    print("\nПроверка типов через isinstance():")
    for bus in fleet:
        if isinstance(bus, TouristBus):
            print(f"  №{bus.route_number} -> туристический")
        elif isinstance(bus, SchoolBus):
            print(f"  №{bus.route_number} -> школьный")
        else:
            print(f"  №{bus.route_number} -> обычный")

    print("\nФильтрация по типу (только туристические):")
    tourist_only = [b for b in fleet if isinstance(b, TouristBus)]
    for bus in tourist_only:
        print(f"  {bus}")

    print("\nФильтрация по типу (только школьные с сопровождающим):")
    safe_school = [b for b in fleet if isinstance(b, SchoolBus) and b.has_supervisor]
    for bus in safe_school:
        print(f"  {bus}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()