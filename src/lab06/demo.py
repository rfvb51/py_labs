"""
Демонстрация работы Generic-коллекции и Protocol.

Сценарии:
1. Базовые операции TypedCollection[T]
2. find(), filter(), map() со сменой типа
3. TypedCollection с ограничениями Displayable и Scorable (Protocol)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab02.model import Bus
from lab03.models import TouristBus, SchoolBus
from lab06.container import TypedCollection, Displayable, Scorable, D, S


# ===== Добавляем методы display() и score() в классы =====

def add_display_method(cls):
    if not hasattr(cls, 'display'):
        def display(self):
            return f"{self.__class__.__name__}: маршрут {self.route_number}, пассажиров {self.passenger_count}"
        cls.display = display
    return cls

add_display_method(Bus)
add_display_method(TouristBus)
add_display_method(SchoolBus)

if not hasattr(Bus, 'score'):
    Bus.score = lambda self: self.load_factor()

if not hasattr(TouristBus, 'score'):
    TouristBus.score = lambda self: self.calculate_fare() / 100

if not hasattr(SchoolBus, 'score'):
    SchoolBus.score = lambda self: self.load_factor() * 0.5


def main():
    print("=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА №6: GENERICS И TYPING")
    print("=" * 70)

    # ===== ПОДГОТОВКА ДАННЫХ =====
    bus1 = Bus(15, 40)
    bus2 = TouristBus(101, 50, True, True)
    bus3 = SchoolBus(22, 35, "городской", True)

    for bus in [bus1, bus2, bus3]:
        bus.start_route()
    bus1.board_passengers(25)
    bus2.board_passengers(40)
    bus3.board_passengers(28)

    # ===== СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ =====
    print("\n1. БАЗОВЫЕ ОПЕРАЦИИ TYPEDCOLLECTION[T]")
    print("-" * 55)

    collection = TypedCollection[Bus]()
    collection.add(bus1)
    collection.add(bus2)
    collection.add(bus3)
    print("Создана TypedCollection[Bus], добавлено 3 автобуса")

    print(f"\nКоллекция:\n{collection}")

    print(f"Длина коллекции: {len(collection)}")
    print(f"Доступ по индексу: collection[0] = {collection[0]}")
    print(f"Итерация: {[b.route_number for b in collection]}")

    # ===== СЦЕНАРИЙ 2: FIND, FILTER, MAP =====
    print("\n2. FIND, FILTER, MAP (СМЕНА ТИПА ЧЕРЕЗ TypeVar R)")
    print("-" * 55)

    found = collection.find(lambda b: b.passenger_count > 30)
    print(f"find() пассажиров > 30: маршрут {found.route_number if found else 'не найден'}")

    not_found = collection.find(lambda b: b.route_number == 999)
    print(f"find() маршрут 999: {not_found if not_found is None else 'найден'}")

    filtered = collection.filter(lambda b: b.capacity >= 40)
    print(f"filter() вместимость >= 40: {len(filtered)} автобуса (маршруты {[b.route_number for b in filtered]})")

    route_numbers = collection.map(lambda b: b.route_number)
    load_factors = collection.map(lambda b: round(b.load_factor(), 1))
    print(f"map() → номера маршрутов (list[int]): {route_numbers}")
    print(f"map() → загрузка (list[float]): {load_factors}")

    # ===== СЦЕНАРИЙ 3: PROTOCOL И ОГРАНИЧЕНИЯ =====
    print("\n3. PROTOCOL И ОГРАНИЧЕНИЯ (Displayable и Scorable)")
    print("-" * 55)

    display_coll = TypedCollection[D]()
    display_coll.add(bus1)
    display_coll.add(bus2)
    display_coll.add(bus3)
    print("TypedCollection[Displayable] - работает с любым объектом, у которого есть display():")
    for item in display_coll:
        print(f"  {item.display()}")

    score_coll = TypedCollection[S]()
    score_coll.add(bus1)
    score_coll.add(bus2)
    score_coll.add(bus3)
    print("\nTypedCollection[Scorable] - работает с любым объектом, у которого есть score():")
    for item in score_coll:
        print(f"  score = {item.score():.1f}")

    sorted_by_score = score_coll.sort_by(lambda b: b.score())
    print(f"\nСортировка по score(): {[round(b.score(), 1) for b in sorted_by_score]}")

    print("\n" + "=" * 70)
    print("ВАЖНО: Классы НЕ наследуют Displayable/Scorable.")
    print("Protocol проверяет наличие методов display() и score() структурно.")


if __name__ == "__main__":
    main()