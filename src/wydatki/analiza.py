from wydatki.kategoryzacja import Kategoryzator
from wydatki.modele import Transakcja


class Analizator:
    def __init__(self, transakcje: list[Transakcja], kategoryzator: Kategoryzator):
        self.transakcje = transakcje
        self.kategoryzator = kategoryzator

    def suma_miesieczna(self):
        raise NotImplementedError

    def suma_wg_kategorii(self):
        raise NotImplementedError
