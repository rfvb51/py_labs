import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import TouristBus, SchoolBus
from lab04.interfaces import Printable, Comparable
from lab02.collection import BusFleet

def print_all(items):
    for item in items:
        print(item.to_string())

def sort_by_income(buses):
    return sorted(buses, key=lambda b: b.calculate_income())

def main():
    print("=" * 70)
    print("ЛАБОРАТОРНАЯ РАБОТА №4: ИНТЕРФЕЙСЫ И АБСТРАКТНЫЕ КЛАССЫ")
    print("=" * 70)

    tourist1 = TouristBus(101, 50, 0, 0, "Анна", 100)
    tourist2 = TouristBus(102, 45, 0, 0, "Максим", 120)
    school = SchoolBus(33, 30, 0, 0, "Школа №7", True)

    tourist1.start_route()
    tourist1.board_passengers(40)
    tourist2.start_route()
    tourist2.board_passengers(35)
    school.start_route()
    school.board_passengers(28)

    print("\nСЦЕНАРИЙ 1: РАЗНЫЕ КЛАССЫ ЧЕРЕЗ ОДИН ИНТЕРФЕЙС PRINTABLE")
    print("-" * 55)
    print_all([tourist1, tourist2, school])

    print("\nСЦЕНАРИЙ 2: ИНТЕРФЕЙС КАК ТИП + СОРТИРОВКА + ISINSTANCE")
    print("-" * 55)
    print("До сортировки:")
    for bus in [tourist1, tourist2]:
        print(f"  {bus.to_string()}")
    
    sorted_buses = sort_by_income([tourist1, tourist2])
    print("\nПосле сортировки по доходу:")
    for bus in sorted_buses:
        print(f"  {bus.to_string()}")
    
    print("\nПроверка isinstance:")
    print(f"  TouristBus implements Printable: {isinstance(tourist1, Printable)}")
    print(f"  TouristBus implements Comparable: {isinstance(tourist1, Comparable)}")
    print(f"  SchoolBus implements Printable: {isinstance(school, Printable)}")
    print(f"  SchoolBus implements Comparable: {isinstance(school, Comparable)}")

    print("\nСЦЕНАРИЙ 3: ИНТЕГРАЦИЯ С КОЛЛЕКЦИЕЙ BUSFLEET")
    print("-" * 55)
    
    fleet = BusFleet()
    fleet.add(tourist1)
    fleet.add(tourist2)
    fleet.add(school)
    
    print(f"Всего автобусов в коллекции: {len(fleet)}")
    
    printable_buses = [b for b in fleet.get_all() if isinstance(b, Printable)]
    comparable_buses = [b for b in fleet.get_all() if isinstance(b, Comparable)]
    
    print(f"\nФильтрация по интерфейсу Printable: {len(printable_buses)} автобусов")
    for bus in printable_buses:
        print(f"  {bus.to_string()}")
    
    print(f"\nФильтрация по интерфейсу Comparable: {len(comparable_buses)} автобусов")
    for bus in comparable_buses:
        print(f"  {bus.__class__.__name__}: доход {bus.calculate_income()} руб.")
    
    print("\nПолиморфизм через интерфейс (без isinstance):")
    for bus in printable_buses:
        print(f"  {bus.to_string()}")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()