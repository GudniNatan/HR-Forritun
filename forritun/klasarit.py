
class Notandi():
    def __init__(self, notendaNafn="", lykilord="", heilsuUpplysingar=dict()):
        self.heilsuUpplysingar = heilsuUpplysingar
        self.notendaNafn = notendaNafn
        self.lykilord = lykilord

class Stadsetning(object):
    def __init__(self, nafn="", gpsHnit=()):
        self.nafn = nafn
        self.gpsHnit = gpsHnit

class Leid():
    def __init__(self, upphafsstadur=Stadsetning(), endapunktur=Stadsetning()):
        self.upphafsstadur = upphafsstadur
        self.endapunktur = endapunktur

class Hjolastigur(Leid):
    def __init__(self, upphafsstadur=Stadsetning(), endapunktur=Stadsetning(), nafn="", medaleinkunn=0.0, fjoldi_einkunna=0):
        super(Hjolastigur, self).__init__(upphafsstadur, endapunktur)
        self.upphafsstadur = upphafsstadur
        self.endapunktur = endapunktur
        self.nafn = nafn
        self.medaleinkunn = medaleinkunn
        self.fjoldi_einkunna = fjoldi_einkunna

class HjolaleidFraAtilB(Leid):
    def __init__(self, upphafsstadur=Stadsetning(), endapunktur=Stadsetning(), hjolastigar=[Hjolastigur()]):
        super(HjolaleidFraAtilB, self).__init__(upphafsstadur, endapunktur)
        self.upphafsstadur = upphafsstadur
        self.endapunktur = endapunktur
        self.hjolastigar = hjolastigar

    def reiknaTima(self, notandi=Notandi()):
        pass