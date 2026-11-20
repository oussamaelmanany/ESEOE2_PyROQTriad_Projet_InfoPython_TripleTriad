#creation et gestion des matrices
tableJeux=[[[],[],[]],[[],[],[]],[[],[],[]]]
mainJoueur_1=["carte1","carte2","carte3","carte4","carte5"]
mainJoueur_2=["carte1","carte2","carte3","carte4","carte5"]
carte_1,carte_2,carte_3,carte_4,carte_5,carte_6,carte_7,carte_8,carte_9,carte_10=""
listeCartes=[carte_1,carte_2,carte_3,carte_4,carte_5,carte_6,carte_7,carte_8,carte_9,carte_10]

def afficheTable(tableJeux):
    for elem in tableJeux:
        print(f"{elem}")
    #print(f"{elem}" for elem in tableJeux)

def tour(joueurActu):   #joueur1 = True et joueur2(bot) = False
    if joueurActu:
        joueurActu=False
    else:
        joueurActu=True

    return joueurActu

def caseTable():
    caseChoisi=int(input("Entrer la case que vous voulez jouer (0-8)"))
    if caseChoisi==0:
        x=0,y=0
    elif caseChoisi==1:
        x=1,y=0
    elif caseChoisi==2:
        x=2,y=0
    elif caseChoisi==3:
        x=0,y=1
    elif caseChoisi==4:
        x=1,y=1
    elif caseChoisi==5:
        x=2,y=1
    elif caseChoisi==6:
        x=0,y=2
    elif caseChoisi==7:
        x=1,y=2
    elif caseChoisi==8:
        x=2,y=2
    
    return caseChoisi

def carteJoue():
    carteActu=int(input("Entrer le numero de la carte que vous voulez jouer (0-4)"))
    return carteActu


def distrib(listeCartes): #A faire quand on aura les classes
    pass

def jeux(tableJeux,mainJoueur_1,mainJoueur_2,joueurActu):
    if joueurActu:
            carteActu=carteJoue
            
            mainJoueur_1[carteActu]
            pass
