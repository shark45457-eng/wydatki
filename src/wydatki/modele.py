from dataclasses import dataclass
from datetime import date


@dataclass
class Transakcja:
    data: date
    opis: str
    kwota: float
    kategoria: str = "inne"
