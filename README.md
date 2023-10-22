# Pendu client/serveur (SAÉ3.02)

Ce projet est issu à la base d'un projet éducatif réalisé par des étudiants. Il s'agit de fameux jeu du pendu en utilisant la méthode de communication client/serveur. Le pendu est un jeu consistant à trouver un mot en devinant quelles sont les lettres qui le composent. Le jeu se joue traditionnellement à deux, avec un papier et un crayon, selon un déroulement bien particulier. Dans notre cas, le serveur imposera les mots à deviner au client qui lui répondra par le biais d’un terminal (CLI = Command-Line Interface).

## Pour commencer

Vous devez vous munir d'un simple ordinateur ayant un système d'exploitation (Windows ou Linux). Cette application utilise l'interface de commande de votre système (terminal) et il n'y a rien besoin de plus pour la faire fonctionner.

### Pré-requis

Voici avant tout les pré-requis pour pouvoir utiliser correctement l'application :

- Avoir un ordinateur sous OS (Windows ou Linux) - MAC OS non compatible
- Se munir de la version la plus récente du projet - Voir rubrique ***Versions***
- Préparer un terminal pour le lancement de l'application (Visual Studio Code ou terminal de l'OS)

### Installation

Avant de pouvoir utiliser notre application, il vous faut installer Python. 

* Sur **Windows** : 

1. Téléchargez la dernière version du programme d'installation exécutable de Python pour Windows x86-64 à partir de la page de [téléchargements](https://www.python.org/downloads/) du site officiel de Python.

2. Exécutez le fichier exécutable du programme d'installation Python que vous avez téléchargé à l'étape précédente.

Sélectionnez les options suivantes dans la fenêtre du programme d'installation de Python pour configurer les étapes d'installation de l'interface de la ligne de commande EB qui suivent.

3. Choisissez d'ajouter l'exécutable Python à votre chemin.

4. Choisissez *Install Now* (Installer maintenant).

* Sur **Linux** :

1. Mettez à jour les paquets de votre distribution Linux (Debian, Ubuntu, Kali Linux, etc...) :
```bash
      sudo apt-get update
      sudo apt-get upgrade
```
2. Installez Python 3 (cela installera la version la plus récente de Python 3.X.X) :
```bash
      sudo apt-get install python3
```
* Si vous utilisez Visual Studio Code, téléchargez simplement les extensions nécessaires pour utiliser Python.

## Démarrage

Pour pouvoir faire focntionner l'application, vous devez procédez de la manière suivante :

* Pour **Windows** :

Dans au moins deux terminaux, taper dans l'un des deux l'éxecutable du fichier serveur avec la commande ``py.exe <nom_fichier>.py`` ou ``.\<nom_fichier>.py``, puis dans l'autre la même commande pour le client.

* Pour **Linux** :

Dans au moins deux terminaux, taper dans l'un des deux l'éxecutable du fichier serveur avec la commande ``python3 <nom_fichier>.py``, puis dans l'autre la même commande pour le client.

* Avec *Visual Studio Code* :

Selon votre système d'exploitation, Visual Studio Code utilise le terminal lié à celui-ci. Effectuez les mêmes méthodes précédentes en fonction de votre OS.

## Fabriqué avec

* [Visual Studio Code](https://code.visualstudio.com/) - Éditeur de codes

## Versions

Veuillez utiliser la version stable de l'application si vous voulez profiter pleinement des fonctionnalités.

* **Dernière version stable :** 

## Auteurs

* **Damien PAYET** _alias_ [@DamienPayet22](https://github.com/DamienPayet22)
* **Bacar SOILIHI** _alias_ [@Bacar7](https://github.com/Bacar7)
* **Aaron PIGRÉE** _alias_ [@aaronp974](https://github.com/aaronp974)

## License

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE](LICENSE) pour plus d'informations