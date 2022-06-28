import datetime


class Database:
    def __init__(self):
        self.data: dict[float, dict[str, int]] = {}

    def insert(self, timestamp: float, data: dict[str, int]):
        self.data[timestamp] = data

    def query(self, interval: int) -> dict[str, int]:
        start_time = datetime.datetime.now().timestamp() - interval
        relevant_timestamps = list(filter(lambda x: x > start_time, self.data))
        result = {}

        for timestamp in relevant_timestamps:
            for keyword, value in self.data[timestamp].items():
                result[keyword] = result.get(keyword, 0) + value
        return result
