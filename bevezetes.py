

'''I/A:
Játékos neve: Gandalf
szerepkör: varázsló
 
I/B:
Üdvözlünk Gandalf, 2 életed van!
    A. Kérje be az alábbi adatokat a fenti mintának megfelelően:
Játékos neve és szerepköre!  (2p)
    B. A program az adatbekérés után írasson ki egy üdvözlést az alábbiak alapján!
Amennyiben „varázsló” a játékosunk, 2 élete van.
Amennyiben „harcos” a játékosunk, 10 életereje van.
Amennyiben ismeretlen a játékosunk szerepköre, 8 életereje van. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)'''

def beker():
    player = []
    player_name = input("Adjma meg a Játékos nevét: ")
    player_class = input("Adja meg a szerepkörét [harcos, varázsló, egyéb]: ")
    player.append(player_name)
    player.append(player_class)
    return player

def konzolra_ir(jatekos):
    print("I/A:")
    print(f"Játékos neve: {jatekos[0]}")
    print(f"szerepkör: {jatekos[1]}")
    print("I/B:")
    if jatekos[1] == "harcos":
        print(f"Üdvözlünk {jatekos[0]}, 10 életed van!")
    elif jatekos[1] == "varázsló" or jatekos[1] == "varazslo":
        print(f"Üdvözlünk {jatekos[0]}, 2 életed van!")
    else:
        print(f"Üdvözlünk {jatekos[0]}, 8 életed van!")

