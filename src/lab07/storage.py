import sys
import os
import json
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab02.model import Bus
from lab03.models import TouristBus, SchoolBus

class Storage:
    @staticmethod
    def save(collection: List[Any], filepath: str) -> None:
        data = []
        for item in collection:
            item_dict = {
                'type': item.__class__.__name__,
                'route_number': item.route_number,
                'capacity': item.capacity,
                'passenger_count': item.passenger_count,
                'current_speed': item.current_speed,
                'state': item.state
            }
            if isinstance(item, TouristBus):
                item_dict['has_wifi'] = item.has_wifi
                item_dict['has_ac'] = item.has_ac
            elif isinstance(item, SchoolBus):
                item_dict['route_type'] = item.route_type
                item_dict['has_supervisor'] = item.has_supervisor
            data.append(item_dict)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def load(filepath: str) -> List[Any]:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            return []
        
        items = []
        for item_dict in data:
            item_type = item_dict['type']
            if item_type == 'Bus':
                item = Bus(
                    item_dict['route_number'],
                    item_dict['capacity'],
                    item_dict['current_speed'],
                    item_dict['passenger_count']
                )
            elif item_type == 'TouristBus':
                item = TouristBus(
                    item_dict['route_number'],
                    item_dict['capacity'],
                    item_dict['has_wifi'],
                    item_dict['has_ac'],
                    item_dict['current_speed'],
                    item_dict['passenger_count']
                )
            elif item_type == 'SchoolBus':
                item = SchoolBus(
                    item_dict['route_number'],
                    item_dict['capacity'],
                    item_dict['route_type'],
                    item_dict['has_supervisor'],
                    item_dict['current_speed'],
                    item_dict['passenger_count']
                )
            else:
                continue
            item._state = item_dict.get('state', 'in_depot')
            items.append(item)
        
        return items