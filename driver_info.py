import json
from dataclasses import dataclass


@dataclass
class Driver:
    id: int
    first_name: str
    last_name: str

    def __init__(self, d_id, first_name, last_name):
        self.id = d_id
        self.last_name = last_name
        self.first_name = first_name

    def get_full_name(self):
        return f"""{self.first_name} {self.last_name}"""


class DriverInfo:
    def __init__(self):
        self.drivers = {}
        self.rides = {}
        self.top_ten = {
            "prompt": [], "clean": [], "friendly": []
        }

        with open('data/drivers.json') as f:
            tmp_drivers = json.load(f)
            for driver in tmp_drivers:
                self.drivers[driver['id']] = {
                    'info': Driver(driver['id'], driver['name'], driver['last_name']),
                    'prompt': 0,
                    'clean': 0,
                    'friendly': 0
                }

        with open('data/ride_info.json') as f:
            tmp_rides = json.load(f)
            for ride in tmp_rides:
                self.rides[ride['id']] = ride

        with open('data/driver_ride.json') as f:
            self.driver_rides = json.load(f)

    def process_data(self):
        for driver_ride in self.driver_rides:
            self.drivers[driver_ride['driver_id']]['prompt'] = \
                self.drivers[driver_ride['driver_id']]['prompt'] + 1 \
                    if not self.rides[driver_ride['ride_id']]['prompt'] else self.drivers[driver_ride['driver_id']][
                    'prompt']
            self.drivers[driver_ride['driver_id']]['clean'] = \
                self.drivers[driver_ride['driver_id']]['clean'] + 1 \
                    if not self.rides[driver_ride['ride_id']]['clean'] else self.drivers[driver_ride['driver_id']][
                    'clean']
            self.drivers[driver_ride['driver_id']]['friendly'] = \
                self.drivers[driver_ride['driver_id']]['friendly'] + 1 \
                    if not self.rides[driver_ride['ride_id']]['friendly'] else self.drivers[driver_ride['driver_id']][
                    'friendly']

            self.top_ten['prompt'] = sorted(self.drivers.values(), key=lambda i: i['prompt'], reverse=True)[:10]
            self.top_ten['clean'] = sorted(self.drivers.values(), key=lambda i: i['clean'], reverse=True)[:10]
            self.top_ten['friendly'] = sorted(self.drivers.values(), key=lambda i: i['friendly'], reverse=True)[:10]

    def get_top_ten(self):
        self.process_data()
        top_ten = {'prompt': [], 'clean': [], 'friendly': []}
        for driver in self.top_ten['prompt']:
            top_ten['prompt'].append({driver['info'].get_full_name(): driver['prompt']})
        for driver in self.top_ten['clean']:
            top_ten['clean'].append({driver['info'].get_full_name(): driver['clean']})
        for driver in self.top_ten['friendly']:
            top_ten['friendly'].append({driver['info'].get_full_name(): driver['friendly']})

        return top_ten
