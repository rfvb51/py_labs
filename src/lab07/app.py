import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List, Optional, Callable, Dict, Any
from lab02.model import Bus
from lab03.models import TouristBus, SchoolBus
from lab05.strategies import by_route_number, by_passenger_count, by_load_factor
from lab06.container import TypedCollection
from exceptions import DuplicateItemError, ItemNotFoundError, InvalidInputError

class BusApp:
    def __init__(self, collection: Optional[TypedCollection] = None):
        self._collection = collection if collection else TypedCollection[Bus]()
    
    def get_all(self) -> List[Bus]:
        return self._collection.get_all()
    
    def add_bus(self, route_number: int, capacity: int) -> Bus:
        for existing in self._collection.get_all():
            if existing.route_number == route_number:
                raise DuplicateItemError(f"Автобус маршрута {route_number} уже существует")
        
        try:
            bus = Bus(route_number, capacity)
            self._collection.add(bus)
            return bus
        except ValueError as e:
            raise InvalidInputError(str(e))
    
    def add_tourist_bus(self, route_number: int, capacity: int, has_wifi: bool, has_ac: bool) -> TouristBus:
        for existing in self._collection.get_all():
            if existing.route_number == route_number:
                raise DuplicateItemError(f"Автобус маршрута {route_number} уже существует")
        
        try:
            bus = TouristBus(route_number, capacity, has_wifi, has_ac)
            self._collection.add(bus)
            return bus
        except ValueError as e:
            raise InvalidInputError(str(e))
    
    def add_school_bus(self, route_number: int, capacity: int, route_type: str, has_supervisor: bool) -> SchoolBus:
        for existing in self._collection.get_all():
            if existing.route_number == route_number:
                raise DuplicateItemError(f"Автобус маршрута {route_number} уже существует")
        
        try:
            bus = SchoolBus(route_number, capacity, route_type, has_supervisor)
            self._collection.add(bus)
            return bus
        except ValueError as e:
            raise InvalidInputError(str(e))
    
    def remove_bus(self, route_number: int) -> None:
        for bus in self._collection.get_all():
            if bus.route_number == route_number:
                self._collection.remove(bus)
                return
        raise ItemNotFoundError(f"Автобус маршрута {route_number} не найден")
    
    def find_by_route_number(self, route_number: int) -> Optional[Bus]:
        for bus in self._collection.get_all():
            if bus.route_number == route_number:
                return bus
        return None
    
    def filter_by(self, predicate: Callable[[Bus], bool]) -> List[Bus]:
        return self._collection.filter(predicate)
    
    def sort_by(self, key_func: Callable[[Bus], any]) -> List[Bus]:
        return self._collection.sort_by(key_func).get_all()
    
    def get_sorted_by_route(self) -> List[Bus]:
        return self.sort_by(by_route_number)
    
    def get_sorted_by_passengers(self) -> List[Bus]:
        return self.sort_by(by_passenger_count)
    
    def get_sorted_by_load(self) -> List[Bus]:
        return self.sort_by(by_load_factor)
    
    def start_route(self, route_number: int) -> None:
        bus = self.find_by_route_number(route_number)
        if not bus:
            raise ItemNotFoundError(f"Автобус маршрута {route_number} не найден")
        bus.start_route()
    
    def board_passengers(self, route_number: int, count: int) -> int:
        bus = self.find_by_route_number(route_number)
        if not bus:
            raise ItemNotFoundError(f"Автобус маршрута {route_number} не найден")
        return bus.board_passengers(count)
    
    def get_collection_for_save(self) -> List[Bus]:
        return self._collection.get_all()