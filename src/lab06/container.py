from typing import TypeVar, Generic, Callable, Optional, Protocol

#TypeVar для Generic-коллекции

T = TypeVar('T')
R = TypeVar('R')

#Protocol для структурной типизации

class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...

#TypeVar с ограничением

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

#Generic-коллекция

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Элемент не найден")
        self._items.remove(item)
    
    def get_all(self) -> list[T]:
        return list(self._items)
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]
    
    def sort_by(self, key_func: Callable[[T], any]) -> 'TypedCollection[T]':
        new_collection = TypedCollection[T]()
        new_collection._items = sorted(self._items, key=key_func)
        return new_collection
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __getitem__(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]
    
    def __iter__(self):
        return iter(self._items)
    
    def __str__(self) -> str:
        if len(self._items) == 0:
            return "Коллекция пуста"
        result = f"Коллекция (всего: {len(self._items)}):\n"
        for i, item in enumerate(self._items):
            result += f"  {i+1}. {item}\n"
        return result