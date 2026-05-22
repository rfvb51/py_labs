import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from app import BusApp
from storage import Storage
from exceptions import DuplicateItemError, ItemNotFoundError, InvalidInputError

class CLI:
    def __init__(self):
        self.app = BusApp()
        self._load_data()
    
    def _load_data(self) -> None:
        try:
            data = Storage.load('buses.json')
            for bus in data:
                self.app._collection.add(bus)
            print(f"Загружено {len(data)} автобусов")
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
    
    def _save_data(self) -> None:
        try:
            Storage.save(self.app.get_collection_for_save(), 'buses.json')
            print("Данные сохранены")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
    
    def _print_menu(self) -> None:
        print("\n" + "=" * 50)
        print("АВТОПАРК - Управление автобусами")
        print("=" * 50)
        print("1. Показать все автобусы")
        print("2. Добавить автобус")
        print("3. Удалить автобус")
        print("4. Найти автобус по маршруту")
        print("5. Фильтрация автобусов")
        print("6. Сортировка автобусов")
        print("7. Отправить на маршрут")
        print("8. Посадить пассажиров")
        print("0. Выход")
        print("-" * 50)
    
    def _get_choice(self) -> int:
        while True:
            try:
                choice = int(input("Выберите пункт: "))
                return choice
            except ValueError:
                print("Ошибка: введите число")
    
    def _show_all(self) -> None:
        buses = self.app.get_all()
        if not buses:
            print("\nАвтопарк пуст")
            return
        
        print("\n" + "-" * 70)
        print(f"{'№':<3} {'Маршрут':<8} {'Вместимость':<12} {'Пассажиры':<10} {'Скорость':<10} {'Состояние':<12}")
        print("-" * 70)
        for i, bus in enumerate(buses, 1):
            print(f"{i:<3} {bus.route_number:<8} {bus.capacity:<12} {bus.passenger_count:<10} {bus.current_speed:<10.1f} {bus.state:<12}")
        print("-" * 70)
    
    def _add_bus(self) -> None:
        print("\n--- Добавление автобуса ---")
        print("Типы автобусов:")
        print("1. Обычный")
        print("2. Туристический")
        print("3. Школьный")
        
        try:
            type_choice = int(input("Выберите тип: "))
            route = int(input("Номер маршрута: "))
            capacity = int(input("Вместимость (1-50): "))
            
            if type_choice == 1:
                bus = self.app.add_bus(route, capacity)
                print(f"Добавлен обычный автобус: {bus}")
            
            elif type_choice == 2:
                wifi = input("Наличие Wi-Fi (y/n): ").lower() == 'y'
                ac = input("Наличие кондиционера (y/n): ").lower() == 'y'
                bus = self.app.add_tourist_bus(route, capacity, wifi, ac)
                print(f"Добавлен туристический автобус: {bus}")
            
            elif type_choice == 3:
                route_type = input("Тип маршрута (городской/пригородный/междугородний): ")
                supervisor = input("Наличие сопровождающего (y/n): ").lower() == 'y'
                bus = self.app.add_school_bus(route, capacity, route_type, supervisor)
                print(f"Добавлен школьный автобус: {bus}")
            
            else:
                print("Неверный тип")
        
        except DuplicateItemError as e:
            print(f"Ошибка: {e}")
        except InvalidInputError as e:
            print(f"Ошибка ввода: {e}")
        except ValueError:
            print("Ошибка: введите корректное число")
    
    def _remove_bus(self) -> None:
        route = int(input("Номер маршрута для удаления: "))
        bus = self.app.find_by_route_number(route)
        
        if not bus:
            print(f"Автобус маршрута {route} не найден")
            return
        
        print(f"Найден автобус: {bus}")
        confirm = input(f"Удалить автобус маршрута {route}? (y/n): ").lower()
        
        if confirm == 'y':
            try:
                self.app.remove_bus(route)
                print("Автобус удалён")
            except ItemNotFoundError as e:
                print(f"Ошибка: {e}")
        else:
            print("Удаление отменено")
    
    def _find_bus(self) -> None:
        route = int(input("Номер маршрута: "))
        bus = self.app.find_by_route_number(route)
        
        if bus:
            print(f"\nНайден автобус: {bus}")
        else:
            print(f"Автобус маршрута {route} не найден")
    
    def _filter_buses(self) -> None:
        print("\n--- Фильтрация ---")
        print("1. По вместимости (мин.)")
        print("2. По количеству пассажиров (мин.)")
        print("3. По типу (туристические)")
        
        choice = input("Выберите фильтр: ")
        
        if choice == '1':
            min_cap = int(input("Минимальная вместимость: "))
            filtered = self.app.filter_by(lambda b: b.capacity >= min_cap)
            print(f"\nНайдено автобусов: {len(filtered)}")
            for b in filtered:
                print(f"  {b}")
        
        elif choice == '2':
            min_pass = int(input("Минимальное количество пассажиров: "))
            filtered = self.app.filter_by(lambda b: b.passenger_count >= min_pass)
            print(f"\nНайдено автобусов: {len(filtered)}")
            for b in filtered:
                print(f"  {b}")
        
        elif choice == '3':
            filtered = self.app.filter_by(lambda b: b.__class__.__name__ == 'TouristBus')
            print(f"\nНайдено туристических автобусов: {len(filtered)}")
            for b in filtered:
                print(f"  {b}")
        
        else:
            print("Неверный выбор")
    
    def _sort_buses(self) -> None:
        print("\n--- Сортировка ---")
        print("1. По номеру маршрута")
        print("2. По количеству пассажиров")
        print("3. По загрузке (%)")
        
        choice = input("Выберите сортировку: ")
        
        if choice == '1':
            sorted_buses = self.app.get_sorted_by_route()
        elif choice == '2':
            sorted_buses = self.app.get_sorted_by_passengers()
        elif choice == '3':
            sorted_buses = self.app.get_sorted_by_load()
        else:
            print("Неверный выбор")
            return
        
        print("\nРезультат сортировки:")
        for b in sorted_buses:
            print(f"  {b}")
    
    def _start_route(self) -> None:
        route = int(input("Номер маршрута: "))
        try:
            self.app.start_route(route)
            print(f"Автобус маршрута {route} отправлен на маршрут")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")
    
    def _board_passengers(self) -> None:
        route = int(input("Номер маршрута: "))
        count = int(input("Количество пассажиров: "))
        
        try:
            boarded = self.app.board_passengers(route, count)
            print(f"Посажено пассажиров: {boarded}")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    def run(self) -> None:
        print("Добро пожаловать в систему управления автопарком!")
        
        while True:
            self._print_menu()
            choice = self._get_choice()
            
            if choice == 1:
                self._show_all()
            elif choice == 2:
                self._add_bus()
            elif choice == 3:
                self._remove_bus()
            elif choice == 4:
                self._find_bus()
            elif choice == 5:
                self._filter_buses()
            elif choice == 6:
                self._sort_buses()
            elif choice == 7:
                self._start_route()
            elif choice == 8:
                self._board_passengers()
            elif choice == 0:
                self._save_data()
                print("До свидания!")
                break
            else:
                print("Неверный пункт меню")