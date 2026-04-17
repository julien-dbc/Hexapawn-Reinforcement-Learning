"""CODE N°1 : CODAGE DU JEU HEXAPAWN """
import random as rd
# Fonction du jeu HEXAPAWN
strategie = {}
def hexapawn ():
    while True:
        position = [[1,2,3], [7,8,9]]
        affiche (position)
        while not (gagnante (position)): 
            valide = False
            while not (valide): # Coup Joueur HU
                coup = input ("Votre coup ou 0 ? ")
                if coup == '0':
                    return
                valide = humain (coup, position)
                if valide: # Vérification de la validité du coup de HU 
                    position = jouer (coup, position, 0)
                else: 
                    print ("Vous ne pouvez pas jouer ca !") 
            if not(gagnante (position)): # Si HU ne gagne pas, alors l'IA joue
                iacherche = rd.choice(jouables(position))
                historique = [key (position)] 
                jouer (str (iacherche), position, 1) 
                historique += [iacherche]
                print(historique)
                if gagnante (position): # Si l'IA gagne
                    print ("Je gagne...")
                    strategie [historique [0]] += [historique [1]]
            else: # Si l'HU gagne
                print( "Vous gagnez...")
                strategie[historique[0]].remove(historique[1])
           

def jouables(position): # Mouvements possibles pour l'IA
    global strategie
    cle = key (position)
    if cle in strategie:
       return strategie[cle]
    [hu,ia]=position
    dep=[]
    for k in ia:
        avancer = k - 3
        if surPlateau (avancer) and avancer not in hu and avancer not in ia:
           dep += [10 * k + avancer]
        droite = k - 2
        if surPlateau (droite) and not (colDroite (k)) and droite in hu:
           dep += [10 * k + droite]
        gauche = k - 4
        if surPlateau (gauche) and not (colGauche (k)) and gauche in hu:
           dep += [10 * k + gauche]
    strategie[cle] = dep
    return dep



def surPlateau(n): 
    return 1 <= n <= 9 

def colDroite (n): 
    return n % 3 == 0

def colGauche (n): 
    return n % 3 == 1

def key (position):
    [hu,ia] = position
    plateau = "" 
    for k in [7,8,9,4,5,6,1,2,3]: 
        if k in hu: plateau += 'O' 
        elif k in ia: plateau += 'X'
        else: plateau += ' '
    return plateau # retourne une chaîne de caractères

def aff (c): print (c, end='')
def affiche (position): # affiche le plateau de jeu
    [hu,ia] = position
    print([hu,ia])
    plateau =""
    for k in [7,8,9,4,5,6,1,2,3]: 
        if k in hu: aff("O")
        elif k in ia: aff("X")
        else: aff(".")
        if k % 3 == 0: print()
    print("-"*10)


def gagnante (position): # Vérifie si HU ou IA remporte la partie
    [hu,ia] = position
    hu.sort ()
    ia.sort () 
    if any ([v in [7,8,9] for v in hu]): 
        return 1
    if any ([v in [1,2,3] for v in ia]): 
        return 1 
    if len (hu) == 0 or len(ia) == 0: 
        return 1
    if len (hu) == len(ia):
        if all ([ia[k] - hu[k] == 3 for k in range(len(hu))]): return 1
    return 0













def humain(coup, position):
    [hu,ia] = position
    [d,a] = [int(v) for v in coup]
    if not(d in hu): return False
    ti = a in ia
    tg = colGauche (d)
    td = colDroite (d)
    tv = not (ti) and not (a in hu)
    if a == d + 3 and tv: return True 
    if a == d + 2 and not (tg) and ti: return True 
    if a == d + 4 and not (td) and ti: return True
    return False
 
def jouer (coup, position, xo):
    global strategie
    [hu, ia] = position
    [d, a] = [int(v) for v in coup]
    if xo == 0:
        hu.remove(d)
        hu += [a]
        if a in ia: ia.remove(a)
    else:
        ia.remove(d)
        ia += [a]
        if a in hu: hu.remove(a)
    print ("Je joue", coup)
    affiche ([hu, ia])
    return [hu, ia]
 
 
 
 
 
 
 
 
 