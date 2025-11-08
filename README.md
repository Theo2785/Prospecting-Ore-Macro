# Prospecting Ore Macro (Roblox)

## French version :

Ce projet est une macro automatisée pour le jeu Prospecting Ore sur Roblox.

Elle permet d’automatiser les actions répétitives de creusage et de remplissage de la pelle dans le jeu, à l’aide d’une interface graphique (GUI) simple.

### Fonctionnalités :

Interface intuitive avec Tkinter (aucune ligne de commande à taper).

Configuration personnalisée :

  -Nombre de coups de pelle à donner.
  
  -Durée de remplissage de la pelle (en secondes).
  

Lancement automatique du cycle après 5 secondes (le temps de revenir dans le jeu).

Possibilité d’arrêter le programme avec Ctrl + C dans la console.

Boutons “Start” et “Quit” dans l’interface graphique.


### Interface graphique

L’application affiche une petite fenêtre avec :

Un champ pour indiquer le nombre de coups de pelle (entre 1 et 20).

Un champ pour la durée du remplissage (entre 0 et 30 secondes).

Les deux bouton "Start" et "Quit"


### Fonctionnement du script

Une fois démarré :

  -Le programme attend 5 secondes pour te laisser revenir dans Roblox.
  
  -Il maintient le clic gauche pour remplir la pelle le nombre de fois indiqué.
  
  -Il avance et recule automatiquement pour simuler le mouvement du joueur.
  
  -Il vide la batée (pan) puis recommence le cycle en boucle.
  
  -Tu peux arrêter le script à tout moment avec Ctrl + C dans la console.



### Installation et utilisation

Installe les dépendances (bash):

> pip install pydirectinput


Lance le script :

python prospecting_macro.py


Renseigne les valeurs et clique sur Start.

Reviens rapidement dans Roblox avant le début du cycle ( 5 sencondes) !

### Avertissement

Cette macro est un outil d’automatisation à usage personnel.
Son utilisation peut enfreindre les règles de Roblox — utilise-la à tes risques et périls.



##  English version :

This project is an automated macro for the Roblox game Prospecting Ore.

It automates the repetitive actions of digging and filling the shovel in the game using a simple graphical interface (GUI).

### Features

Intuitive interface built with Tkinter (no command line required).

Custom configuration:

  -Number of shovel hits.
  
  -Shovel filling duration (in seconds).
  
Automatic start of the cycle after 5 seconds (time to switch back to the game).

Ability to stop the program at any time with Ctrl + C in the console.

“Start” and “Quit” buttons in the GUI.


### Graphical Interface

The application displays a small window with:

A field to set the number of shovel hits (between 1 and 20).

A field to set the filling duration (between 0 and 30 seconds).

Two buttons: “Start” and “Quit”.


### How It Works

Once started:

The program waits 5 seconds to let you switch back to Roblox.

It holds the left mouse button to fill the shovel the specified number of times.

It moves forward and backward automatically to simulate player movement.

It empties the pan (batée) and repeats the cycle in a loop.

You can stop the script anytime with Ctrl + C in the console.

### Installation & Usage

Install dependencies (bash):

> pip install pydirectinput


Run the script:

python prospecting_macro.py


Enter your values and click Start.
Quickly switch back to Roblox before the cycle begins (5 seconds)!

### Disclaimer

This macro is an automation tool for personal use only.
Its use may violate Roblox’s terms of service — use it at your own risk.
