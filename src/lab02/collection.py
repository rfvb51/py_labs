from model import Bus

class BusFleet:
    def __init__(self):
        self._buses = []

    def add(self, bus):
        if not isinstance(bus, Bus):
            raise TypeError("в коллекцию можно добавлять только Bus")
        if self.find_by_route_number(bus.route_number) is not None:
            raise ValueError("автобус с таким номером маршрута уже есть")
        self._buses.append(bus)

    def remove(self, bus):
        if bus in self._buses:
            self._buses.remove(bus)
            return True
        return False

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("индекс должен быть целым числом")
        if index < 0 or index >= len(self._buses):
            raise IndexError("индекс вне диапазона")
        return self._buses.pop(index)

    def get_all(self):
        return list(self._buses)

    def find_by_route_number(self, route_number):
        for bus in self._buses:
            if bus.route_number == route_number:
                return bus
        return None

    def find_by_state(self, state):
        result = BusFleet()
        for bus in self._buses:
            if bus.state == state:
                result.add(bus)
        return result

    def find_by_load_factor_range(self, min_factor, max_factor):
        result = BusFleet()
        for bus in self._buses:
            factor = bus.load_factor()
            if min_factor <= factor <= max_factor:
                result.add(bus)
        return result

    def sort_by_route_number(self):
        self._buses.sort(key=lambda bus: bus.route_number)

    def sort_by_load_factor(self, reverse=True):
        self._buses.sort(key=lambda bus: bus.load_factor(), reverse=reverse)

    def get_on_route(self):
        return self.find_by_state("on_route")

    def get_in_depot(self):
        return self.find_by_state("in_depot")

    def get_available_for_route(self):
        result = BusFleet()
        for bus in self._buses:
            if bus.state == "in_depot" and bus.free_seats() > 0:
                result.add(bus)
        return result

    def __len__(self):
        return len(self._buses)

    def __iter__(self):
        return iter(self._buses)

    def __getitem__(self, index):
        if isinstance(index, slice):
            result = BusFleet()
            for bus in self._buses[index]:
                result.add(bus)
            return result
        if not isinstance(index, int):
            raise TypeError("индекс должен быть целым числом")
        if index < 0 or index >= len(self._buses):
            raise IndexError("индекс вне диапазона")
        return self._buses[index]

    def __contains__(self, bus):
        return bus in self._buses

    def __str__(self):
        if len(self._buses) == 0:
            return "Автопарк пуст"
        result = f"Автопарк (всего автобусов: {len(self._buses)}):\n"
        for i, bus in enumerate(self._buses):
            result += f"  {i + 1}. {bus}\n"
        return result