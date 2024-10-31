# POC: HelloWorld avec NASM et Python

Ce projet combine un programme simple en assembleur NASM qui affiche "Hello, World!" dans le terminal, et un script Python qui récupère la sortie de ce programme pour le faire défiler dans une fenetre

## Prérequis

Avant d'exécuter ou de recompiler ce projet, il est nécessaire d'installer les dépendances suivantes sur un système Ubuntu :

1. **NASM** : Assembleur utilisé pour compiler le code assembleur.

   Installez NASM avec la commande :
   ```bash
   sudo apt-get install nasm
   ```

2. **Bibliothèques 32 bits** : Le projet utilise des instructions et un assembleur pour une architecture 32 bits. Il est donc nécessaire d'avoir les bibliothèques multilib installées pour le lien et la compilation.

   Installez les bibliothèques 32 bits avec la commande :
   ```bash
   sudo apt-get install gcc-multilib
   ```

3. **Tkinter** : Utilisé pour créer l'interface graphique Python.

   Installez Tkinter avec la commande :
   ```bash
   sudo apt-get install python3-tk
   ```

## Compilation

Un binaire déjà compiler est fournis. Mais il est possible de repartir de zéro et de recompiler soit-meme l'executable en tapant:
    ```bash
    make clean
    ```

Le projet inclut un `Makefile` pour faciliter la compilation du programme assembleur. Voici les étapes pour compiler et exécuter le projet.

1. **Compiler l'assembleur :**

   Pour compiler le fichier assembleur `hello.asm`, utilisez la commande `make` à partir du répertoire racine du projet :
   ```bash
   make
   ```

   Cette commande va :
   - Utiliser **NASM** pour assembler le fichier source en un fichier objet dans le répertoire `obj`.
   - Lier le fichier objet et produire l'exécutable final dans le répertoire `bin`.

3. **Exécuter l'exécutable :**
   Une fois compilé, vous pouvez lancer l'exécutable manuellement :
   ```bash
   ./bin/hello
   ```

## Exécuter le script Python avec interface graphique

Le script Python `main.py` permet d'exécuter l'exécutable assembleur et d'afficher le message "Hello, World!" dans une fenêtre graphique avec une animation.

Pour exécuter le script Python, utilisez la commande suivante :
```bash
python3 main.py
```

## Remarques

- Le programme assembleur a été compilé et testé sur Ubuntu. Il est configuré pour une architecture 32 bits. Si vous travaillez sur un système 64 bits, assurez-vous d'avoir installé les bibliothèques 32 bits avec `gcc-multilib` comme mentionné plus haut.
- Si vous rencontrez des problèmes lors de l'exécution du script Python, vérifiez que **Tkinter** est correctement installé sur votre système.

