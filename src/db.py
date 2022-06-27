import datetime

test_data = {
    datetime.datetime.now().timestamp() - 30: {'email': 7, 'checkpoint': 2},
    datetime.datetime.now().timestamp() - 60: {'email': 10, 'security': 10},
    datetime.datetime.now().timestamp() - 90: {'checkpoint': 4},
    datetime.datetime.now().timestamp() - 120: {'avanan': 8, 'email': 4},
    datetime.datetime.now().timestamp() - 150: {'security': 2, 'email': 3, 'avanan': 4},
    datetime.datetime.now().timestamp() - 180: {'security': 7, 'avanan': 6},
    datetime.datetime.now().timestamp() - 210: {'checkpoint': 6, 'avanan': 1},
    datetime.datetime.now().timestamp() - 240: {'checkpoint': 6, 'email': 2},
    datetime.datetime.now().timestamp() - 270: {'checkpoint': 2, 'avanan': 3, 'security': 4},
    datetime.datetime.now().timestamp() - 300: {'avanan': 4}
}


class Database:
    def __init__(self):
        self.data: dict[float, dict[str, int]] = test_data

    def insert(self, timestamp: float, data: dict[str, int]):
        if len(data.keys()) == 0:
            return

        if timestamp in self.data:
            # TODO
            self.data[timestamp] = {**self.data[timestamp], **data}
            return

        self.data[timestamp] = data

    def query(self, interval: int) -> dict[str, int]:
        start_time = datetime.datetime.now().timestamp() - interval
        data = [data for timestamp, data in self.data.items() if timestamp >= start_time]
        result = {}
        for record in data:
            for key, value in record.items():
                result[key] = result.get(key, 0) + value
        return result
