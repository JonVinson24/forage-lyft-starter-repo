from abc import ABC
from datetime import datetime

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date: datetime, warning_light_is_on: bool) -> None:
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
