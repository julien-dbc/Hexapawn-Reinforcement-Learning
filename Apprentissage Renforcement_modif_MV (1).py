#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:04:31 2023

@author: julien.dbc
"""
import random as rd

strategie = {}
positions_gagnantes_ia = []
positions_gagnantes_hu = []
gagne = [0, 0] 
def hexapawn ():
    global gagne
    c=0
    while 'XXX   000' not in positions_gagnantes_ia:
        position = [[1,2,3], [7,8,9]]
        while not (gagnante (position)):
            valide = False
            while not (valide):
                coup = rd.choice(jouables_hu(position))
                valide = humain (str(coup), position)
                if valide: 
                    position = jouer (str(coup), position, 0)
                else: 
                    print ("Vous ne pouvez pas jouer ca !") 
            if not(gagnante (position)) and not(key(position) in positions_gagnantes_hu):
                iacherche = rd.choice(jouables_ia(position))
                """
                print(strategie)
                print(iacherche)"""
                historique = [key (position)] 
                position = jouer (str (iacherche), position, 1) 
                historique += [iacherche]
                if gagnante(position) or key(position) in positions_gagnantes_ia:
                    if gagnante(position):
                        gagne [1] += 1
                        vainqueur = 'ia'
                        if not(key(position)+'*' in positions_gagnantes_ia):
                            positions_gagnantes_ia.append(key(position)+'*')
                    strategie [historique [0]] += [historique [1]]
                    L = strategie[historique[0]]
                    if all([x == L[0] for x in L]):
                        if historique[0] not in positions_gagnantes_ia:
                            positions_gagnantes_ia.append(historique[0]) 
            else:
                if gagnante(position):
                    gagne [0] += 1
                    vainqueur = 'hu'
                    if not(key(position)+'*' in positions_gagnantes_hu):
                        positions_gagnantes_hu.append(key(position)+'*')
                if len(strategie[historique[0]]) != 0:
                    strategie[historique[0]].remove(historique[1])
                    L = strategie[historique[0]]
                    if len(L) == 0:
                        positions_gagnantes_hu.append(historique[0])    
        c = c+1
    print(c,' parties' )
    print ('Le score est :' , gagne)
    print(strategie)
    print('positions gagnantes pour IA : ', positions_gagnantes_ia)
    print('positions gagnantes pour HU : ',positions_gagnantes_hu)
           
def jouables_hu(position):
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


def jouables_ia(position):
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
    return plateau


def gagnante (position):
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
    if not(d in hu): 
        return False
    ti = a in ia
    tg = colGauche (d)
    td = colDroite (d)
    tv = not (ti) and not (a in hu)
    if a == d + 3 and tv: 
        return True 
    if a == d + 2 and not (tg) and ti: 
        return True 
    if a == d + 4 and not (td) and ti: 
        return True
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
    return [hu, ia]
 
 
 
 
 
 
 
 
 