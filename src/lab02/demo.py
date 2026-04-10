from model import Bus
from collection import BusFleet

def main():
    fleet = BusFleet()

    print("=== БАЗОВАЯ РАБОТА С КОЛЛЕКЦИЕЙ ===")
    bus1 = Bus(15, 40)
    bus2 = Bus(22, 35)
    bus3 = Bus(101, 50)

    fleet.add(bus1)
    fleet.add(bus2)
    fleet.add(bus3)
    print("После добавления:", fleet)

    try:
        fleet.add(Bus(22, 35))
    except ValueError as e:
        print("Ошибка дубликата:", e)

    try:
        fleet.add("не автобус")
    except TypeError as e:
        print("Ошибка типа:", e)

    fleet.remove(bus2)
    print("После удаления bus2:", fleet)

    # ПОИСК, ИТЕРАЦИЯ, ИНДЕКСАЦИЯ
    print("\n=== ПОИСК, ИТЕРАЦИЯ, ИНДЕКСАЦИЯ ===")
    bus1.start_route()
    bus1.board_passengers(25)

    print("Поиск по номеру 15:", fleet.find_by_route_number(15))
    print("Автобусы на маршруте:", list(fleet.get_on_route()))

    print("Итерация:")
    for i, bus in enumerate(fleet):
        print(f"  [{i}] {bus.route_number}: {bus.state}")

    print("Доступ по индексу: fleet[0] =", fleet[0])
    print("Длина коллекции:", len(fleet))

    print("\n=== СОРТИРОВКА И ФИЛЬТРАЦИЯ ===")
    bus4 = Bus(8, 30)
    bus5 = Bus(50, 45)
    fleet.add(bus4)
    fleet.add(bus5)

    bus4.start_route()
    bus4.board_passengers(28)
    bus5.start_route()
    bus5.board_passengers(20)

    print("До сортировки по загрузке:")
    for bus in fleet:
        print(f"  {bus.route_number}: загрузка {bus.load_factor()}%")

    fleet.sort_by_load_factor(reverse=True)
    print("После сортировки (по убыванию загрузки):")
    for bus in fleet:
        print(f"  {bus.route_number}: загрузка {bus.load_factor()}%")

    print("Автобусы с загрузкой 50-80%:", list(fleet.find_by_load_factor_range(50, 80)))
    print("Готовые к выходу (депо + свободные места):", list(fleet.get_available_for_route()))

if __name__ == "__main__":
    main()
