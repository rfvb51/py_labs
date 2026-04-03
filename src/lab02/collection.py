from model import Bus

class BusFleet:
    def __init__(self):
        self._buses = []
        self._id_counter = 1

    def add(self, bus):
        if not isinstance(bus, Bus):
            raise TypeError("можно добавлять только объекты Bus")
        for existing in self._buses:
            if existing.route_number == bus.route_number:
                raise ValueError("автобус с таким номером маршрута уже существует")
        self._buses.append(bus)
        return bus

    def remove(self, bus):
        if bus not in self._buses:
            raise ValueError("автобус не найден в коллекции")
        self._buses.remove(bus)

    def remove_at(self, index):
        if index < 0 or index >= len(self._buses):
            raise IndexError("индекс вне диапазона")
        return self._buses.pop(index)

    def get_all(self):
        return self._buses.copy()

    def find_by_route_number(self, route_number):
        result = []
        for bus in self._buses:
            if bus.route_number == route_number:
                result.append(bus)
        return result

    def find_by_state(self, state):
        result = []
        for bus in self._buses:
            if bus.state == state:
                result.append(bus)
        return result

    def find_by_load_factor_range(self, min_factor, max_factor):
        result = []
        for bus in self._buses:
            factor = bus.load_factor()
            if min_factor <= factor <= max_factor:
                result.append(bus)
        return result

    def sort_by_route_number(self):
        self._buses.sort(key=lambda bus: bus.route_number)

    def sort_by_load_factor(self):
        self._buses.sort(key=lambda bus: bus.load_factor(), reverse=True)

    def sort_by_passenger_count(self):
        self._buses.sort(key=lambda bus: bus.passenger_count, reverse=True)

    def get_on_route(self):
        new_fleet = BusFleet()
        for bus in self._buses:
            if bus.state == "on_route":
                new_fleet.add(bus)
        return new_fleet

    def get_in_depot(self):
        new_fleet = BusFleet()
        for bus in self._buses:
            if bus.state == "in_depot":
                new_fleet.add(bus)
        return new_fleet

    def get_available_for_route(self):
        new_fleet = BusFleet()
        for bus in self._buses:
            if bus.state == "in_depot" and bus.free_seats() > 0:
                new_fleet.add(bus)
        return new_fleet

    def __len__(self):
        return len(self._buses)

    def __getitem__(self, index):
        if isinstance(index, slice):
            new_fleet = BusFleet()
            for bus in self._buses[index]:
                new_fleet.add(bus)
            return new_fleet
        if index < 0 or index >= len(self._buses):
            raise IndexError("индекс вне диапазона")
        return self._buses[index]

    def __iter__(self):
        return iter(self._buses)

    def __contains__(self, bus):
        return bus in self._buses

    def __str__(self):
        if len(self._buses) == 0:
            return "Автопарк пуст"
        result = "Автопарк (всего автобусов: " + str(len(self._buses)) + "):\n"
        for i, bus in enumerate(self._buses):
            result += "  " + str(i + 1) + ". " + str(bus) + "\n"
        return result