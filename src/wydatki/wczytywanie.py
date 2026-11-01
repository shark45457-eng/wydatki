from abc import ABC, abstractmethod
from pathlib import Path

from wydatki.modele import Transakcja


class Importer(ABC):
    @abstractmethod
    def wczytaj(self, sciezka: Path) -> list[Transakcja]:
        """Wczytuje plik i zwraca listę transakcji."""


class CsvImporter(Importer):
    def wczytaj(self, sciezka: Path) -> list[Transakcja]:
        raise NotImplementedError


class ExcelImporter(Importer):
    def wczytaj(self, sciezka: Path) -> list[Transakcja]:
        raise NotImplementedError
