from datetime import datetime
from abc import ABC
from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> None:
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
