import datetime


class Database:
    def __init__(self):
        self.data: dict[float, dict[str, int]] = {}

    def insert(self, timestamp: float, data: dict[str, int]):
        self.data[timestamp] = data

    def query(self, interval: int) -> dict[str, int]:
        start_time = datetime.datetime.now().timestamp() - interval
        data = [data for timestamp, data in self.data.items() if timestamp >= start_time]
        result = {}
        for record in data:
            for key, value in record.items():
                result[key] = result.get(key, 0) + value
        return result
