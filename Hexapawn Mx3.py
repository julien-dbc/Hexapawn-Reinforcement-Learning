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

            if not gagnante(position, 1 - joueur)[0]: # Si HU ne gagne pas, alors l'IA joue
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



def coups_possibles(position, joueur):
    coups = []
    if joueur == 0:  # Joueur humain
        coups = jouables_hu(position)
    elif joueur == 1:  # IA
        coups = jouables_ia(position)
    return coups



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


def aff(c):
    print(c, end='')






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
        print("Unexpected format of coup:", coup)
        return False




def jouer(coup, position, joueur):
    hu = position[0].copy()
    ia = position[1].copy()
    d, a = coup  
    if joueur == 0:  # Joueur humain
        if d in hu:
            hu.remove(d)
            hu.append(a)
            if a in ia:
                ia.remove(a)
    else:  # IA
        if d in ia:
            ia.remove(d)
            ia.append(a)
            if a in hu:
                hu.remove(a)
    return [hu, ia]




