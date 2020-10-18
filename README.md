[<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/images/logo.png" width="200px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

Norminette EPITECH développé avec les fonctionnalités de la dernière mise à jour de la norme d'EPITECH pour la promotion 2025. Disponible pour tous les étudiants.
La norminette cherche les erreurs de norme d'Epitech dans le code source des fichiers.

## Menu

* __[Installation et utilisation](#bubulle)__
  * [Dépendances](#dépendances)
  * [Installation de la norminette](#installation)
  * [Utilisation](#utilisation)
* __[Options](#options)__
* __[Fonctionnalités](#features)__

## bubulle

### Dépendances
  Pour utiliser la norminette Bubulle, vous devez avoir Python 3.x installé sur votre ordinateur.
 - [Python](https://python.com)

#### Installation
```
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)"
```
## Utilisation

  Ecrivez simplement la commande suivante dans votre terminal, dans le dossier où se situe le code que vous souhaitez vérifier : 
 `bubulle`

## Options

 - `-p` ou `--path`: lancer la norminette dans un dossier précis

## Features

 - Détection des lignes trop grandes (plus de 80 colonnes sur une seule ligne)
 - Détection des espaces manquants dans les assignations ou comparaison de variables
 - Vérification des fichiers inutiles
 - Détection des espaces en trop sur une ligne et en fin de fichier
 - Vérification des fichiers qui ne sont pas en accord avec la convention snake_case
 - Vérification des fichiers sources qui n'ont pas pour extension .c ni .h
 - Vérification des noms de fichiers qui ne sont pas clairs (par exemple: test.c, string.c ...)
 - Vérification des fichiers sources vides
 - Détection des accolades ouvrantes mal positionnées pour les fonctions
 - Détection des accolades ouvrantes mal positionnées pour les mots clés for, while, if
 - Détection des éventuelles fonctions de la libC interdites dans le sujet
 - Détection du mot clé 'goto' interdit
 - Détection des fonctions avec trop de lignes à l'intérieur de celles-ci (plus de 20 lignes)
 - Détection des fonctions mal nommées (ne respectant pas notamment la convention snake_case)
 - Détection des déclarations de fonctions possédant plus de 4 paramètres
 - Vérification du header EPITECH par la norminette dans les fichiers sources
 - Vérification de l'indentation : les tabs sont interdits, ils doivent être remplacés par quatre espaces.
 - Détection des lignes en trop (deux lignes ou plus vides par exemple)
 - Détection des macros utilisées pour des constantes : elles doivent servir pour remplacer des fonctions en une ligne
 - Détection des espaces manquants entre les virgules
 - Détection des assignements de variables multiples sur une seule et même ligne
 - Vérification des variables ne respectant pas la convention snake_case
 - Détection de la norme du nom d'un typedef, qui doit se terminer par _t
