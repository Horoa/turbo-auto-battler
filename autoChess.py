from random import choice

def jeu():
    pv=30
    argent=5
    creatures = []
    creatures.append(Creature("Gobelin", "G", 1, 1, 1, 1, 1, 1))
    creatures.append(Creature("Loup", "L", 1, 1, 2, 1, 1, 1))
    creatures.append(Creature("Humain", "H", 1, 1, 1, 1, 1, 1))
    
    plateau=[ ["" for i in range(12)] for j in range(12)]
    terrain=["" for i in range(12)]
    shop=[choice(creatures) for i in range(12)]
    afficherUUI(pv,argent)
    afficher(plateau)
    afficherTab(terrain)
    afficherTab(shop)

class Creature():
    def __init__(self, name, icone, prix, attaque, vitesse, vitesseAttaque, portee, niveau): 
        self.name = name
        self.icone = icone
        self.prix = prix
        self.attaque = attaque
        self.vitesse = vitesse
        self.vitesseAttaque = vitesseAttaque
        self.portee = portee
        self.niveau = niveau
        
class Shop():
    def __init__(self, level, creatures, money, moneyMax, priceUp):
        self.level = level
        self.creatures = creatures
        self.money = money
        self.moneyMax = moneyMax
        self.priceUp = priceUp


def afficherUUI(pv, argent):
    print("  - - - - - - - - - - - -")
    print("| pv = " + str(pv) + " | argent = " + str(argent) + "   |")

    
def afficher(plateau):
    print("  - - - - - - - - - - - -")
    for ligne in plateau:
        print("|",end='')
        for cellule in ligne:
            if cellule=="":
                print(" ", end='')
            else :
                print(str(plateau[i][j].icone),end='')
            print(" ",end='')
        print("|")
    print("  - - - - - - - - - - - -")

def afficherTab(plateau):
    print("|",end='')
    for i in range(len(plateau)) :
        if plateau[i]=="":
            print(" ", end='')
        else :
            print(str(plateau[i].icone),end='')
        print(" ",end='')
    print("|")
    print("  - - - - - - - - - - - -")
    
jeu()

