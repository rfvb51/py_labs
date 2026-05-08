import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab02.collection import BusFleet

class AdvancedBusCollection(BusFleet):
    
    def sort_by(self, key_func):
        new_collection = AdvancedBusCollection()
        new_collection._buses = sorted(self._buses, key=key_func)
        return new_collection
    
    def filter_by(self, predicate):
        new_collection = AdvancedBusCollection()
        for bus in self._buses:
            if predicate(bus):
                new_collection.add(bus)
        return new_collection
    
    def apply(self, func):
        new_collection = AdvancedBusCollection()
        for bus in self._buses:
            result = func(bus)
            new_collection.add(result)
        return new_collection
    
    def map(self, func):
        return list(map(func, self._buses))
    
    def __str__(self):
        if len(self._buses) == 0:
            return "Коллекция пуста"
        return "\n".join(str(b) for b in self._buses)