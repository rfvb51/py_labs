from model import Bus
from collection import BusFleet

def print_separator(title):
    print("\n" + "=" * 70)
    print(" " + title)
    print("=" * 70)

def main():
    print_separator("ЛАБОРАТОРНАЯ РАБОТА №2: КОЛЛЕКЦИЯ BUSFLEET")

    fleet = BusFleet()

    print_separator("СЦЕНАРИЙ 1: СОЗДАНИЕ И ДОБАВЛЕНИЕ АВТОБУСОВ")

    bus1 = Bus(15, 40)
    bus2 = Bus(22, 35)
    bus3 = Bus(101, 50)
    bus4 = Bus(8, 30)

    print("Созданы автобусы:")
    print("  " + str(bus1))
    print("  " + str(bus2))
    print("  " + str(bus3))
    print("  " + str(bus4))

    fleet.add(bus1)
    fleet.add(bus2)
    fleet.add(bus3)
    fleet.add(bus4)

    print("\nАвтобусы добавлены в автопарк")
    print(fleet)

    print_separator("СЦЕНАРИЙ 2: ОГРАНИЧЕНИЕ НА ДУБЛИКАТЫ")

    print("Попытка добавить автобус с существующим номером маршрута (22):")
    try:
        bus_duplicate = Bus(22, 35)
        fleet.add(bus_duplicate)
    except ValueError as e:
        print("  Ошибка: " + str(e))

    print("\nПопытка добавить объект неправильного типа:")
    try:
        fleet.add("не автобус")
    except TypeError as e:
        print("  Ошибка: " + str(e))

    print_separator("СЦЕНАРИЙ 3: ИЗМЕНЕНИЕ СОСТОЯНИЯ АВТОБУСОВ")

    print("Автобус №15 выходит на маршрут:")
    bus1.start_route()
    print("  " + str(bus1))

    print("\nАвтобус №22 выходит на маршрут:")
    bus2.start_route()
    print("  " + str(bus2))

    print("\nАвтобус №15 набирает пассажиров (25 человек):")
    bus1.board_passengers(25)
    print("  " + str(bus1))

    print("\nАвтобус №22 набирает пассажиров (30 человек):")
    bus2.board_passengers(30)
    print("  " + str(bus2))

    print("\nАвтобус №8 отправляется на ТО:")
    bus4.send_to_maintenance()
    print("  " + str(bus4))

    print(fleet)

    print_separator("СЦЕНАРИЙ 4: ПОИСК И ФИЛЬТРАЦИЯ")

    print("Поиск автобусов на маршруте (on_route):")
    on_route = fleet.find_by_state("on_route")
    for bus in on_route:
        print("  " + str(bus))

    print("\nПоиск автобусов по номеру маршрута 101:")
    found = fleet.find_by_route_number(101)
    for bus in found:
        print("  " + str(bus))

    print("\nПоиск автобусов с загрузкой от 60% до 80%:")
    load_range = fleet.find_by_load_factor_range(60, 80)
    for bus in load_range:
        print("  " + str(bus))

    print_separator("СЦЕНАРИЙ 5: ИТЕРАЦИЯ И ИНДЕКСАЦИЯ")

    print("Итерация по коллекции с помощью for:")
    for i, bus in enumerate(fleet):
        print("  [" + str(i) + "] " + str(bus))

    print("\nДоступ по индексу:")
    print("  fleet[0] -> " + str(fleet[0]))
    print("  fleet[2] -> " + str(fleet[2]))

    print("\nСрез коллекции fleet[1:3]:")
    slice_fleet = fleet[1:3]
    print(slice_fleet)

    print("\nДлина коллекции: " + str(len(fleet)))

    print_separator("СЦЕНАРИЙ 6: СОРТИРОВКА")

    print("Сортировка по номеру маршрута:")
    fleet.sort_by_route_number()
    print(fleet)

    print("Сортировка по загрузке (от наибольшей):")
    fleet.sort_by_load_factor()
    print(fleet)

    print_separator("СЦЕНАРИЙ 7: ЛОГИЧЕСКИЕ ОПЕРАЦИИ")

    print("Автобусы на маршруте (get_on_route):")
    on_route_fleet = fleet.get_on_route()
    print(on_route_fleet)

    print("Автобусы в депо (get_in_depot):")
    depot_fleet = fleet.get_in_depot()
    print(depot_fleet)

    print("Автобусы, готовые к выходу на маршрут (get_available_for_route):")
    available_fleet = fleet.get_available_for_route()
    print(available_fleet)

    print_separator("СЦЕНАРИЙ 8: УДАЛЕНИЕ")

    print("Удаление автобуса по индексу 2 (до удаления):")
    print("  " + str(fleet[2]))
    removed = fleet.remove_at(2)
    print("Удален: " + str(removed))
    print("\nКоллекция после удаления:")
    print(fleet)

    print("Удаление автобуса по объекту:")
    fleet.remove(bus2)
    print(fleet)

    print_separator("ИТОГОВОЕ СОСТОЯНИЕ КОЛЛЕКЦИИ")
    print(fleet)
    print("Всего операций выполнено: создание, добавление, изменение состояния, поиск, итерация, индексация, сортировка, фильтрация, удаление")

if __name__ == "__main__":
    main()