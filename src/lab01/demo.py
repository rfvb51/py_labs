from model import Bus


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_case(title):
    print()
    print(title)
    print("-" * len(title))


def print_error(text):
    print(f"Ошибка: {text}")


def main():
    print_section("1. Создание объектов и вывод информации (__str__)")
    try:
        bus1 = Bus(5, 40)
        bus2 = Bus(12, 30)
        print(bus1)
        print(bus2)
    except Exception as e:
        print_error(str(e))

    print_section("2. Проверка валидации при создании (некорректные данные)")
    try:
        print("Попытка создать автобус №-5:")
        bus_invalid = Bus(-5, 40)
    except Exception as e:
        print_error(str(e))

    try:
        print("Попытка создать автобус вместимостью 60:")
        bus_invalid = Bus(10, 60)
    except Exception as e:
        print_error(str(e))

    try:
        print("Попытка создать автобус с пассажирами в депо:")
        bus_invalid = Bus(10, 40, 0, 10)
    except Exception as e:
        print_error(str(e))

    print_section("3. Изменение состояния и работа с пассажирами")
    try:
        bus = Bus(25, 50)
        print("Начальное состояние:")
        print(bus)

        print("\nВыход на маршрут...")
        bus.start_route()
        print(bus)

        print("\nПосадка 30 пассажиров:")
        boarded = bus.board_passengers(30)
        print(f"Село: {boarded}")
        print(bus)

        print("\nПопытка высадки 10 пассажиров:")
        alighted = bus.alight_passengers(10)
        print(f"Высадилось: {alighted}")
        print(bus)

        print("\nПопытка посадки 25 пассажиров (осталось мест 20):")
        boarded = bus.board_passengers(25)
        print(f"Село: {boarded}")
        print(bus)

        print("\nВозвращение в депо (сначала высадим всех):")
        bus.alight_passengers(bus.passenger_count)
        bus.return_to_depot()
        print(bus)

    except Exception as e:
        print_error(str(e))

    print_section("4. Изменение скорости (setter с валидацией)")
    try:
        bus = Bus(7, 40)
        bus.start_route()
        print("После выхода на маршрут:")
        print(bus)

        print("\nУвеличиваем скорость до 60 км/ч...")
        bus.current_speed = 60
        print(bus)

        print("\nПопытка установить скорость 150 км/ч (превышение MAX_SPEED):")
        bus.current_speed = 150
    except Exception as e:
        print_error(str(e))

    print_section("5. Проверка логических состояний")
    try:
        bus = Bus(9, 35)
        print(bus)

        print("\nОтправляем на ТО...")
        bus.send_to_maintenance()
        print(bus)

        print("\nПопытка выехать на маршрут с ТО:")
        bus.start_route()
    except Exception as e:
        print_error(str(e))

    try:
        print("\nЗавершаем ТО и возвращаем в депо...")
        bus.repair_complete()
        print(bus)

        print("\nВыход на маршрут...")
        bus.start_route()
        print(bus)

        print("\nПосадка пассажиров...")
        bus.board_passengers(10)
        print(bus)

        print("\nПопытка уехать в депо с пассажирами:")
        bus.return_to_depot()
    except Exception as e:
        print_error(str(e))

    print_section("6. Сравнение объектов (__eq__)")
    try:
        bus_a = Bus(1, 40)
        bus_b = Bus(1, 40)
        bus_c = Bus(2, 40)

        print(f"bus_a: {bus_a}")
        print(f"bus_b: {bus_b}")
        print(f"bus_c: {bus_c}")

        print(f"\nbus_a == bus_b: {bus_a == bus_b}")
        print(f"bus_a == bus_c: {bus_a == bus_c}")
        print(f"bus_a == 'Автобус': {bus_a == 'Автобус'}")
    except Exception as e:
        print_error(str(e))

    print_section("7. Демонстрация __repr__")
    try:
        bus = Bus(15, 45)
        print("Строка для разработчика (__repr__):")
        print(repr(bus))
        print("\nВоссоздание объекта из __repr__ (концептуально):")
        new_bus = eval(repr(bus))
        print(f"Воссозданный объект: {new_bus}")
        print(f"Исходный и воссозданный объекты равны: {bus == new_bus}")
    except Exception as e:
        print_error(str(e))

    print_section("8. Демонстрация атрибута класса")
    try:
        bus1 = Bus(1, 40)
        bus2 = Bus(2, 30)

        print(f"Атрибут класса Bus.MAX_SPEED: {Bus.MAX_SPEED}")
        print(f"Доступ через экземпляр bus1.MAX_SPEED: {bus1.MAX_SPEED}")
        print(f"Доступ через экземпляр bus2.MAX_SPEED: {bus2.MAX_SPEED}")

        print("\nИзменение атрибута класса:")
        Bus.MAX_SPEED = 100
        print(f"Новый Bus.MAX_SPEED: {Bus.MAX_SPEED}")
        print(f"bus1.MAX_SPEED: {bus1.MAX_SPEED}")
        print(f"bus2.MAX_SPEED: {bus2.MAX_SPEED}")
    except Exception as e:
        print_error(str(e))

    print_section("9. Дополнительные бизнес-методы (free_seats, load_factor)")
    try:
        bus = Bus(33, 50)
        bus.start_route()
        bus.board_passengers(42)

        print(bus)
        print(f"Свободных мест: {bus.free_seats()}")
        print(f"Коэффициент загрузки: {bus.load_factor()}%")
    except Exception as e:
        print_error(str(e))


if __name__ == "__main__":
    main()