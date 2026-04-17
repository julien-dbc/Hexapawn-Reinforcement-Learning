# ♟️ AI for Hexapawn (Reinforcement Learning)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Machine_Learning-FF6F00?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Machine Learning" />
  <img src="https://img.shields.io/badge/Reinforcement_Learning-0052CC?style=for-the-badge&logo=databricks&logoColor=white" alt="Reinforcement Learning" />
  <img src="https://img.shields.io/badge/Game_Theory-4CAF50?style=for-the-badge&logo=strategy&logoColor=white" alt="Game Theory" />
</div>

---

## 🇬🇧 English Version

### 📖 Overview
* 🎯 **Challenge:** Build an Artificial Intelligence capable of mastering a board game from scratch without any pre-programmed strategies or heuristics.
* 🛠️ **Solution:** Developed a complete Hexapawn game engine in Python. Implemented a reinforcement learning algorithm where the AI learns purely through trial and error. The system records game states, rewards winning paths, and "prunes" losing branches from its strategy dictionary.
* 📈 **Impact:** Successfully trained a model capable of perfect play. Expanded the project by scaling the board size ($M \times 3$) and implemented an algorithm to generate a complete game tree, allowing for instant win-state calculation and strategy optimization.

### 🧠 Core Concepts & Algorithms

The project explores fundamental AI concepts using the game of Hexapawn (a simplified variant of chess played with pawns).

* **The Game Engine:** A custom Python environment (`Hexapawn.py`) handles board representation, valid move generation (moving forward, capturing diagonally), and win-condition checking for both Human and AI players.
* **Reinforcement Learning (MENACE Model):** The core AI learns by playing. It stores a dictionary (`strategie`) mapping board states to possible moves. When the AI loses, the last move it made from the preceding state is removed (punishment). Over time, only winning or drawing moves remain, leading to a perfect strategy.
* **Scaling the Board:** The game mechanics were generalized (`Hexapawn Mx3.py`) to handle arbitrary board sizes ($M \times 3$), allowing testing of how the state space complexity affects the learning rate.
* **Game Tree Generation:** Developed an algorithm to recursively build the complete game tree (`graphecomplet`). This allows the system to exhaustively map every possible game state and definitively determine the winning player from any given position, eliminating the need for iterative learning once the tree is built.

### 💻 Code Structure
The repository contains several iterations of the AI logic:
* `Hexapawn.py`: The base game engine and the interactive reinforcement learning loop (Human vs. AI).
* `Apprentissage Renforcement_modif_MV.py`: Automated training scripts where the AI plays against itself or random players to rapidly populate its strategy dictionary.
* `Hexapawn Mx3.py` & `J.py`: Generalized versions of the game engine that support dynamic board sizes.

### 📂 Documentation & Media
* **Presentation:** Included is a comprehensive slide deck (`TIPE_DIAPO DUBUC JULIEN (1).pdf`) that visually explains the game rules, the reinforcement learning process, and the game tree generation algorithm.
* **Media:** A video demonstration (`ia.mp4`) showcases the AI's gameplay.

### ⚖️ Copyright & License
This project was developed as part of a TIPE (Travail d'Initiative Personnelle Encadré) research project. The code and presentation materials are intended for educational demonstration within this portfolio.

---
---

## 🇫🇷 Version Française

### 📖 Vue d'ensemble
* 🎯 **Défi :** Construire une Intelligence Artificielle capable de maîtriser un jeu de plateau en partant de zéro, sans aucune stratégie ou heuristique préprogrammée.
* 🛠️ **Solution :** Développement d'un moteur de jeu Hexapawn complet en Python. Implémentation d'un algorithme d'apprentissage par renforcement où l'IA apprend uniquement par essais et erreurs. Le système enregistre les états de jeu, récompense les chemins gagnants et "élague" les branches perdantes de son dictionnaire de stratégies.
* 📈 **Impact :** Entraînement réussi d'un modèle capable d'un jeu parfait. Élargissement du projet en modifiant la taille du plateau ($M \times 3$) et implémentation d'un algorithme pour générer un arbre de jeu complet, permettant le calcul instantané des états gagnants et l'optimisation de la stratégie.

### 🧠 Concepts Clés & Algorithmes

Le projet explore des concepts fondamentaux de l'IA à travers le jeu Hexapawn (une variante simplifiée des échecs jouée uniquement avec des pions).

* **Le Moteur de Jeu :** Un environnement Python sur mesure (`Hexapawn.py`) gère la représentation du plateau, la génération des coups valides (avancer, capturer en diagonale) et la vérification des conditions de victoire pour l'Humain et l'IA.
* **Apprentissage par Renforcement (Modèle MENACE) :** L'IA centrale apprend en jouant. Elle stocke un dictionnaire (`strategie`) associant les états du plateau aux coups possibles. Lorsque l'IA perd, le dernier coup joué depuis l'état précédent est supprimé (punition). Au fil du temps, seuls les coups gagnants ou menant à un match nul subsistent, aboutissant à une stratégie parfaite.
* **Mise à l'échelle du Plateau :** Les mécaniques de jeu ont été généralisées (`Hexapawn Mx3.py`) pour gérer des plateaux de taille arbitraire ($M \times 3$), permettant de tester comment la complexité de l'espace d'états affecte la vitesse d'apprentissage.
* **Génération de l'Arbre de Jeu :** Développement d'un algorithme pour construire récursivement l'arbre de jeu complet (`graphecomplet`). Cela permet au système de cartographier de manière exhaustive chaque état de jeu possible et de déterminer définitivement le joueur gagnant à partir de n'importe quelle position, éliminant ainsi le besoin d'un apprentissage itératif une fois l'arbre construit.

### 💻 Structure du Code
Le dépôt contient plusieurs itérations de la logique de l'IA :
* `Hexapawn.py` : Le moteur de jeu de base et la boucle d'apprentissage par renforcement interactive (Humain contre IA).
* `Apprentissage Renforcement_modif_MV.py` : Scripts d'entraînement automatisés où l'IA joue contre elle-même ou des joueurs aléatoires pour remplir rapidement son dictionnaire de stratégies.
* `Hexapawn Mx3.py` & `J.py` : Versions généralisées du moteur de jeu supportant des tailles de plateau dynamiques.

### 📂 Documentation & Médias
* **Présentation :** Un diaporama complet (`TIPE_DIAPO DUBUC JULIEN (1).pdf`) est inclus, expliquant visuellement les règles du jeu, le processus d'apprentissage par renforcement et l'algorithme de génération de l'arbre de jeu.
* **Médias :** Une vidéo de démonstration (`ia.mp4`) illustre les performances de l'IA en jeu.

### ⚖️ Droits d'auteur & Licence
Ce projet a été développé dans le cadre d'un projet de recherche TIPE (Travail d'Initiative Personnelle Encadré). Le code et les supports de présentation sont destinés à une démonstration éducative au sein de ce portfolio.
