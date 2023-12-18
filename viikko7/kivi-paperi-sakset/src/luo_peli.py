from kivi_paperi_sakset import KiviPaperiSakset
from kps_tekoaly import KPSTekoaly
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

muistin_koko = 10

def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KiviPaperiSakset()
    if tyyppi == 'b':
        return KPSTekoaly(Tekoaly())
    if tyyppi == 'c':
        return KPSTekoaly(TekoalyParannettu(muistin_koko))

    return None
