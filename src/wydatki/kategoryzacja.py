class Kategoryzator:
    def __init__(self, reguly: dict[str, list[str]]):
        self.reguly = reguly

    def kategoryzuj(self, opis: str) -> str:
        opis = opis.lower()
        for kategoria, slowa in self.reguly.items():
            if any(slowo in opis for slowo in slowa):
                return kategoria
        return "inne"
