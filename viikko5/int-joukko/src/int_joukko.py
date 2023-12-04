KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti and (not isinstance(kapasiteetti, int) or kapasiteetti < 0):
            raise Exception("Epäkelpo kapasiteetti.")

        self.kapasiteetti = kapasiteetti if kapasiteetti else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko else OLETUSKASVATUS
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0


    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if self.alkioiden_lkm == 0 or not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_lista(self.ljono, taulukko_old)
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)
            return True
        return False

    def poista(self, n):
        loytyi = False
        for kohta in range(0, self.alkioiden_lkm):
            if n == self.ljono[kohta]:
                loytyi = True
                self.ljono[kohta] = 0
                self.alkioiden_lkm -= 1
            elif loytyi:
                apu = self.ljono[kohta-1]
                self.ljono[kohta-1] = self.ljono[kohta]
                self.ljono[kohta] = apu
        return loytyi


    def kopioi_lista(self, a, b):
        for alkio in range(0, len(a)):
            b[alkio] = a[alkio]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        ret = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for a in range(0, len(a_taulu)):
            ret.lisaa(a_taulu[a])
        for b in range(0, len(b_taulu)):
            ret.lisaa(b_taulu[b])
        return ret

    @staticmethod
    def leikkaus(a, b):
        ret = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for a in range(0, len(a_taulu)):
            for b in range(0, len(b_taulu)):
                if a_taulu[a] == b_taulu[b]:
                    ret.lisaa(b_taulu[b])
        return ret

    @staticmethod
    def erotus(a, b):
        ret = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for a in range(0, len(a_taulu)):
            ret.lisaa(a_taulu[a])
        for b in range(0, len(b_taulu)):
            ret.poista(b_taulu[b])
        return ret

    def __str__(self):
        tuotos = "{" + ", ".join([str(alkio) for alkio in self.ljono[:self.alkioiden_lkm]]) + "}"
        return tuotos
