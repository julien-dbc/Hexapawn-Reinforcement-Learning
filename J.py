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
 
 




















"""CODE N°2 : APPRENTISSAGE PAR RENFORCEMENT"""
import random as rd

strategie = {}

def hexapawn ():
     gagne = [0, 0] 
     c=0
     while c<20:
         position = [[1,2,3], [7,8,9]]
         while not (gagnante (position)):
             valide = False
             while not (valide): # Coup Joueur HU
                 coup = rd.choice(jouables_hu(position))
                 valide = humain (str(coup), position)
                 if valide: # Vérification de la validité du coup de HU 
                     position = jouer (str(coup), position, 0)
                 else: 
                     print ("Vous ne pouvez pas jouer ca !") 
             if not(gagnante (position)): # Si HU ne gagne pas,  l'IA joue
                 
                 iacherche = rd.choice(jouables_ia(position))
                 historique = [key (position)] 
                 position = jouer (str (iacherche), position, 1) 
                 historique += [iacherche]
                 if gagnante (position): # Si l'IA gagne
                     gagne [1] += 1
                     vainqueur = 'ia'
                     strategie [historique [0]] += [historique [1]]
             else: #Si l'HU gagne
                 gagne [0] += 1
                 vainqueur = 'hu'
                 strategie[historique[0]].remove(historique[1])
         c = c+1
         print('partie',c,': ',vainqueur )
     print ('Le score est :' , gagne)
     print('Le taux de victoire est :', (gagne[1]/c)*100)
     print(strategie)
            
def jouables_hu(position): # Mouvements possibles pour l'HU
     [hu,ia]=position
     dep=[]
     for k in hu:
         avancer = k + 3
         if surPlateau (avancer) and avancer not in ia and avancer not in hu:
            dep += [10 * k + avancer]
         gauche = k + 2
         if surPlateau (gauche) and not (colGauche (k)) and gauche in ia:
            dep += [10 * k + gauche]
         droite = k + 4
         if surPlateau (droite) and not (colDroite (k)) and droite in ia:
            dep += [10 * k + droite]
     return dep


def jouables_ia(position): # Mouvements possibles pour l'IA
     global strategie
     cle = key (position)
     if cle in strategie:
        return strategie[cle]
     [hu,ia]=position
     dep=[]
     for k in ia:
         avancer = k - 3
         if surPlateau ( avancer) and avancer not in hu and avancer not in ia:
            dep += [10 * k + avancer]
         droite = k - 2
         if surPlateau (droite) and not (colDroite (k)) and droite in hu:
            dep += [10 * k + droite]
         gauche = k - 4
         if surPlateau (gauche) and not (colGauche (k)) and gauche in hu:
            dep += [10 * k + gauche]
     strategie[cle] = dep
     return dep

'''   Avec les fonctions définies précédemment : 
surPlateau(n) ; colDroite (n) ; colGauche (n) ; key (position) ; 
gagnante(position,joueur) ; humain(coup, position) ; 
jouer(coup, position, joueur)
'''
 


























 
 
"""CODE N°3 : CRÉATION D'UN ARBRE DE JEU (DICTIONNAIRE)"""
import random as rd

gagne = [0, 0] 
def hexapawn ():
    global gagne
    c=0
    while c<20:
        position = [[1,2,3], [7,8,9]]
        joueur=0
        vainqueur = None
        while gagnante(position,1-joueur)[0]==0:
            valide = False
            while not (valide):  # Coup Joueur HU
                coup = rd.choice(jouables_hu(position))
                valide = humain (str(coup), position)
                if valide: # Vérification de la validité du coup de HU 
                    position = jouer (str(coup), position, 0)
                    joueur =1
                else: 
                    print ("Vous ne pouvez pas jouer ca !") 
            
            if gagnante(position,1-joueur)[0]==0: # Si HU ne gagne pas,l'IA joue
                iacherche = coup_gagnant_ia(position)
                position = jouer (str (iacherche), position, 1) 
                joueur =0
                
                if gagnante(position,1-joueur)[0]==1: # Si l'IA gagne
                    gagne [1] += 1
                    vainqueur = 'ia'
            else: # Si l'HU gagne

                gagne [0] += 1
                vainqueur = 'hu'
         
        c = c+1
        print('partie',c,': ',vainqueur)
    print ('Le score est :' , gagne) 
 
def coups_possibles(position, joueur):
    coups = []
    if joueur == 0:  # Joueur humain
        coups = jouables_hu(position)
    elif joueur == 1:  # IA
        coups = jouables_ia(position)
    return coups

def coup_gagnant_ia(position):
    if key(position) in D:
        return D[key(position)][0]
    else:
        return rd.choice(jouables_ia(position))


D = {}
def graphecomplet(position, joueur):
    global D
    if gagnante(position,1-joueur)[0]:
        joueur_gagnant = gagnante(position,1-joueur)[1]
        if joueur_gagnant == 'hu': 
            return [key(position),'hu',-1,[]]
        else:
            return [key(position),'ia',1,[]]
    else:
        coups = coups_possibles(position, joueur)
        if joueur == 0: 
            L = [key(position),'hu',1]
            for coup in coups:
                nouvelle_position = jouer(str(coup), position, joueur)
                T = graphecomplet(nouvelle_position, 1-joueur)
                L.append(T)
                if T[2] == -1:
                    L[2] = -1
        if joueur == 1: 
            L = [key(position),'ia',-1]
            for coup in coups:
                nouvelle_position = jouer(str(coup), position, joueur)
                T = graphecomplet(nouvelle_position, 1-joueur)
                L.append(T)
                if T[2] == 1:
                    L[2] = 1
                    if key(position) not in D:
                        D[key(position)] = [coup]
    return L

'''   Avec les fonctions définies précédemment : 
jouables_hu(position) ; jouables_ia(position) ; affiche (position) ; 
surPlateau(n) ; colDroite (n) ; colGauche (n) ; key (position) ; 
gagnante(position,joueur) ; humain(coup, position) ; 
jouer(coup, position, joueur)
'''
















"""CODE N°4 : AUGMENTATION DE LA TAILLE DU PLATEAU (ENTIER M)"""
import random as rd
M = 3 #longueur du plateau
strategie = {}

def hexapawn():
    gagne = [0, 0]
    c = 0
    while c < 50: # 50 parties
        position = [list(range(1, M+1)), list(range(2*M+1, 3*M+1))]
        joueur = 0
        vainqueur = None
        while not gagnante(position, 1-joueur)[0]:
            valide = False
            while not valide:  # Coup Joueur HU
                coups_possibles = jouables_hu(position)
                coup = rd.choice(coups_possibles)
                valide = humain(coup, position)
                if valide: # Vérification de la validité du coup de HU 
                    position = jouer(coup, position, 0)
                    joueur = 1
                else:
                    print("Vous ne pouvez pas jouer ça !")

            if not gagnante(position, 1 - joueur)[0]: # Si HU ne gagne pas, l'IA joue
                iacherche = rd.choice(jouables_ia(position))
                historique = [key(position)]
                position = jouer(iacherche, position, 1)
                historique += [iacherche]
                joueur = 0
        # Déterminer le vainqueur à la fin de la partie
        if gagnante(position, 1 - joueur)[0]:
            if joueur == 0:
                vainqueur = 'hu'
            else:
                vainqueur = 'ia'
                strategie.setdefault(historique[0], []).append(historique[1])
        else:
            if joueur == 0:
                vainqueur = 'ia'
            else:
                vainqueur = 'hu'
        # Mettre à jour le score
        if vainqueur == 'hu':
            gagne[0] += 1
        elif vainqueur == 'ia':
            gagne[1] += 1

        c += 1
        print('partie', c, ': ', vainqueur)
    print('Le score est :', gagne)
    print('Le taux de victoire est :', (gagne[1]/c)*100)
    print(strategie)

def jouables_hu(position): # Mouvements possibles pour l'HU
    [hu, ia] = position
    dep = []
    for k in hu:
        avancer = k + M
        gauche = k + M - 1
        droite = k + M + 1
        if surPlateau(avancer) and avancer not in ia and avancer not in hu:
            dep.append((k, avancer))
        if surPlateau(gauche) and not (colGauche(k)) and gauche in ia:
            dep.append((k, gauche))
        if surPlateau(droite) and not (colDroite(k)) and droite in ia:
            dep.append((k, droite))
    return dep

def jouables_ia(position): # Mouvements possibles pour l'IA
    [hu, ia] = position
    dep = []
    for k in ia:
        avancer = k - M
        droite = k - (M-1)
        gauche = k - (M+1)
        if surPlateau(avancer) and avancer not in hu and avancer not in ia:
            dep.append((k,avancer))
        if surPlateau(droite) and not (colDroite(k)) and droite in hu:
            dep.append((k,droite))
        if surPlateau(gauche) and not (colGauche(k)) and gauche in hu:
            dep.append((k,gauche))
    return dep

def affiche(position):
    [hu, ia] = position
    plateau = ""
    for k in list(range(1,3*M+1)):
        if k in hu:
            aff("O")
        elif k in ia:
            aff("X")
        else:
            aff(".")
        if k % 3 == 0:
            print()
    print("-" * 10)

def surPlateau(n):
    return 1 <= n <= 3*M
def colDroite(n):
    return n % M == 0
def colGauche(n):
    return n % M == 1




def key(position):
    [hu, ia] = position
    plateau = ""
    for k in list(range(1,3*M+1)):
        if k in hu:
            plateau += 'O'
        elif k in ia:
            plateau += 'X'
        else:
            plateau += ' '
    return plateau

def gagnante(position, joueur):
    [hu, ia] = position
    hu.sort()
    ia.sort()
    if any([v in list(range(2*M+1,3*M+1)) for v in hu]):
        return 1, 'hu'
    if any([v in list(range(1,M+1)) for v in ia]):
        return 1, 'ia'
    if len(hu) == 0:
        return 1, 'ia'
    if len(ia) == 0:
        return 1, 'hu'
    if len(hu) == len(ia):
        if all([ia[k] - hu[k] == M for k in range(len(hu))]):
            if joueur == 0:
                return 1, 'hu'
            else:
                return 1, 'ia'
    return 0, ''

def humain(coup, position):
    [hu, ia] = position
    if isinstance(coup, tuple) and len(coup) == 2:
        d, a = coup  
        if not (d in hu):
            return False
        ti = a in ia
        tg = colGauche(d)
        td = colDroite(d)
        tv = not (ti) and not (a in hu)
        if a == d + M and tv:
            return True
        if a == d + M - 1 and not (tg) and ti:
            return True
        if a == d + M + 1 and not (td) and ti:
            return True
    else:
        return False
'''   Avec les fonctions définies précédemment : 
affiche (position) ;  coups_possibles(position, joueur) ;
jouer(coup, position, joueur)'''