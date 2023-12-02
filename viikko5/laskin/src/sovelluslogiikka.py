class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset_arvot = []

    def miinus(self, operandi):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._edelliset_arvot.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        if self._edelliset_arvot:
            self._arvo = self._edelliset_arvot.pop()

    def onko_kumottavaa(self):
        ret = True if self._edelliset_arvot else False
        return ret


class Summa:

    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        if self.syote():
            self.sovelluslogiikka.plus(int(self.syote()))


class Erotus:

    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        if self.syote():
            self.sovelluslogiikka.miinus(int(self.syote()))


class Nollaus:

    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:

    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.kumoa()



