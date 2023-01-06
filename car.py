from datetime import datetime
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date: datetime) -> None:
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass
