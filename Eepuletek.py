'''Az epulet.txt állomány szerkezete:
·         az épület neve: pl: Centrum LIM
·         az épület városa: pl.: Varsó
·         az épület országa: pl.: Lengyelország
·         az épület magassága m-ben: pl.: 140
·         az épület emeleteinek a száma, pl.: 43
    • az épület építésének az éve, pl.1949'''


class Epuletek:
    def __init__(self, sor):
        self.nev = str(sor[0])
        self.varos = str(sor[1])
        self.orszag = str(sor[2])
        self.magassag = float(sor[3])
        self.emeletek = int(sor[4])
        self.epites_eve = int(sor[5])