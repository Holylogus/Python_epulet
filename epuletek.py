from Eepuletek import  Epuletek

'''Az epulet.txt forrásállomány, épületek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Az epulet.txt állomány szerkezete:
·         az épület neve: pl: Centrum LIM
·         az épület városa: pl.: Varsó
·         az épület országa: pl.: Lengyelország
·         az épület magassága m-ben: pl.: 140
·         az épület emeleteinek a száma, pl.: 43
    • az épület építésének az éve, pl.1949
Az állomány első sora a mezőneveket tartalmazza „$” jellel elválasztva.
A megoldás mintája:
III/A, B:
            	Az épületek száma: 8
III/C:
            	Az 555 lábnál magasabb épületek száma: 2.
III/D:
            	A legöregebb épület országa: Lengyelország.
    A. Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a epulet.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
    B. Írassa ki az épületek számát a mintának megfelelően a konzolra! (2p)
    C. Adja meg az 555 lábnál magasabb épületek számát, ha 1 m = 3.280839895 láb! (4p)
    D. Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)'''

def fajl_beolvas():
    file = open("epulet.txt", "r", encoding="UTF-8", errors="ignore")
    file.readline()
    sorok = file.readlines()
    file.close()
    epuletek = []
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        epuletek.append(Epuletek(sor))
        i += 1
    return epuletek

def epuletek_szama(osztaly):
    print("III/A, B:")
    print(f"Az épületek száma: {len(osztaly)}")

def magas(osztaly):
    hatar = 555/3.280839895
    darab = 0
    i = 0
    while i < len(osztaly):
        if osztaly[i].magassag > hatar:
            darab += 1
            i += 1
        else:
            i += 1
    print("III/C:")
    print(f"Az 555 lábnál magasabb épületek száma: {darab}")


def legoregebb(osztaly):
    i = 0
    min_ertek= osztaly[0].epites_eve
    index = 0
    while i < len(osztaly):
        if osztaly[i].epites_eve < min_ertek:
            index = i
            i += 1
        else:
            i += 1
    print("III/D:")
    print(f"A legöregebb épület országa: {osztaly[index].orszag}")



