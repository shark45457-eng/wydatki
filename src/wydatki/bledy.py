class BladAnalizatora(Exception):
    """Bazowy wyjątek aplikacji."""


class BladFormatu(BladAnalizatora):
    """Brak wymaganych kolumn lub uszkodzony plik."""


class BladDanych(BladAnalizatora):
    """Niepoprawna data lub kwota w wierszu."""


class BladKategoryzacji(BladAnalizatora):
    """Niepoprawne reguły kategorii."""
