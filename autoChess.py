from random import choice

def jeu():
    pv=30
    argent=5
    
    plateau=[ ["" for i in range(12)] for j in range(12)]
    terrain=["" for i in range(12)]
    shop=[choice(creatures) for i in range(12)]
    afficherUUI(pv,argent)
    afficher(plateau)
    afficherTab(terrain)
    afficherTab(shop)

class Creature():
    def __init__(self, name, icone, prix, vie,vieMax, attaque, vitesse, vitesseAttaque, portee, niveau): 
        self.name = name
        self.icone = icone
        self.prix = prix
        self.vie = vie
        self.vieMax = vieMax
        self.attaque = attaque
        self.vitesse = vitesse
        self.vitesseAttaque = vitesseAttaque
        self.portee = portee
        self.niveau = niveau
        self.estVivant = True
        
    def attaque(self,creature):
        creature.subit(creature, self.attaque)
        
    def subit(self,degats):
        self.vie = max(self.vie-degats,0)
        if self.vie == 0:
            self.meurt(self)
            
    def meurt(self):
        self.estVivant = False
        
    def soigne(self,soin):
        self.vie = min(self.vie + soin, self.vieMax)
      
    def soigneFull(self):
        self.vie=self.vieMax
        
        
class Shop():
    def __init__(self, level, sizeMax, creatures, money, moneyMax, priceUp, priceReroll):
        self.level = level
        self.sizeMax = sizeMax
        self.creatures = creatures
        self.money = money
        self.moneyMax = moneyMax
        self.priceUp = priceUp
        self.priceReroll = priceReroll
        
        
class Reserve():
    def __init__(self, level, sizeMax, creatures, money, moneyMax, priceUp):
        self.level = level
        self.sizeMax = sizeMax
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

