import random

'''II/A, B, C:
           	FEJ-ÍRÁS-ÍRÁS-ÍRÁS-FEJ-ÍRÁS-ÍRÁS
II/D, E:
           	A fejek száma: 2.  	
A fejek.txt tartalma:
II/F:
A fejek száma: 2. 	
 
    A. Írasson ki a konzolra kötőjellel (-) elválasztva 7 pénzérmével való dobást véletlen számsorozat alapján a mintának megfelelően! (4p)
    B. A generált értékeket tárolja lista adatszerkezetben logikai típusokkal (0: írás, 1: fej)! (1p)
    C. A „–” jel csak az értékek között szerepeljen (a végén ne)! (2p)
    D. Írjon függvényt fejek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami fej (1). A visszatérési érték legyen egy egész szám! (3p)
    E. A fejek_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
    F. A fejek_szama függvény eredményét írassa ki a mintának megfelelően a fejek.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)'''

def veletlen():
    sorozat = []
    fej_iras = []
    i = 0
    while i < 7:
        sorozat.append(int(random.random()*2))
        i += 1
    return sorozat

def konzolra_ir(lista, darab):
    i = 0
    szoveg = ""
    while i < len(lista)-1:
        if lista[i] == 0:
            szoveg += "FEJ"+"-"
            i += 1
        else:
            szoveg += "ÍRÁS" + "-"
            i +=1
    if lista[i] == 0:
        szoveg += "FEJ"
    else:
        szoveg += "ÍRÁS"
    print("II/A, B, C:")
    print(szoveg)
    print("II/D, E:")
    print(f"A fejek száma: {darab}")

def fejek_szama(lista):
    i = 0
    darab = 0
    while i < len(lista):
        if lista[i] == 0:
            darab += 1
            i += 1
        else:
            i +=1
    return darab

def file_kiir(filenev, darab):
    file = open(filenev, "w", encoding="UTF-8")
    file.write("II/F:\n")
    file.write(f"A fejek száma: {darab}")

