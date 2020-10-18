[<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/images/logo.png" width="200px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

Norminette EPITECH développé avec les fonctionnalités de la dernière mise à jour de la norme d'EPITECH pour la promotion 2025. Disponible pour tous les étudiants.
La norminette cherche les erreurs de norme d'Epitech dans le code source des fichiers.

## Menu

* __[Installation et utilisation](#bubulle)__
  * [Dépendances](#dépendances)
  * [Installation de la norminette](#installation)
  * [Utilisation](#utilisation)
* __[Options](#options)__
* __[Fonctionnalités](#fonctionnalités)__
* __[TODO](#todo)__
* __[Contributeurs](#contributeurs)__

## bubulle

### Dépendances
  Pour utiliser la norminette Bubulle, vous devez avoir Python 3.x et pycparser installé sur votre ordinateur.
 - [Python](https://python.com)
 - Pycparser : ```pip install pycparser``` (installé automatiquement avec le script

#### Installation

L'installation peut s'effectuer directement avec le script d'installation. Le script supprime l'ancienne version et télécharge la nouvelle. C'est la façon la plus facile d'installer la norminette sous Linux. Testé avec le dump Fedora d'EPITECH.

```
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)"
```

Installation manuelle sous Windows : cloner le repository.

## Utilisation

  Ecrivez simplement la commande suivante dans votre terminal, dans le dossier où se situe le code que vous souhaitez vérifier : 
 `bubulle`
 
 Exemple de retour :

[<img alt="Norminette" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/images/example1.png" width="570px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

## Options

 - `-p` ou `--path`: lancer la norminette dans un dossier précis

## Fonctionnalités

### Vérification des fichiers
 - Vérification des fichiers qui ne sont pas en accord avec la convention snake_case
 - Vérification des fichiers sources qui n'ont pas pour extension .c ni .h
 - Vérification des fichiers inutiles
 - Vérification des fichiers sources vides
 - Vérification des noms de fichiers qui ne sont pas clairs (par exemple: test.c, string.c ...)
 
### Vérification de convention de norme

 - Détection des éventuelles fonctions de la libC interdites dans le sujet
 - Détection du mot clé 'goto' interdit
 - Détection des fonctions mal nommées (ne respectant pas notamment la convention snake_case)
 - Vérification du header EPITECH par la norminette dans les fichiers sources
 - Vérification des variables ne respectant pas la convention snake_case
 - Détection de la norme du nom d'un typedef, qui doit se terminer par _t

### Vérification de style du code

 - Détection des lignes trop grandes (plus de 80 colonnes sur une seule ligne)
 - Détection des espaces manquants dans les assignations ou comparaison de variables
 - Détection des espaces en trop sur une ligne et en fin de fichier
 - Détection des accolades ouvrantes mal positionnées pour les fonctions
 - Détection des accolades ouvrantes mal positionnées pour les mots clés for, while, if
 - Détection des fonctions avec trop de lignes à l'intérieur de celles-ci (plus de 20 lignes)
 - Détection des déclarations de fonctions possédant plus de 4 paramètres
 - Vérification de l'indentation : les tabs sont interdits, ils doivent être remplacés par quatre espaces.
 - Détection des lignes en trop (deux lignes ou plus vides par exemple)
 - Détection des macros utilisées pour des constantes : elles doivent servir pour remplacer des fonctions en une ligne
 - Détection des espaces manquants entre les virgules
 - Détection des assignements de variables multiples sur une seule et même ligne
 - Détection des commentaires dans les fonctions
 - Détection des nested fonctions
 
## TODO

 Certaines vérifications/détections ne sont pas encore totalement terminées ou doivent être sujettes à des modifications. Bubulle est une norminette pour EPITECH mise à niveau et à jour avec le dernier Coding Style. C'est la plus complète à ce jour, mais certaines vérifications doivent être achevées :
 
 - Vérification de l'indentation complète de chaque ligne
 - G5 : Vérification des fonctions statiques à utiliser uniquement dans la compilation
 - L6 : Sépération d'une ligne entre la déclaration des variables et le reste du contenu d'une fonction
 - F1 : Cohérence des fonctions ??
 - L6 : Vérification de la déclaration des variables en début de fonction uniquement
 - H2 : Vérification anti double-inclusion des headers
 - H1 : Vérification du contenu des headers (prototypes, structures et macros uniquement)
 - Quelques INFO...

# Contributeurs
 - aureliancnx : Développeur de la Bubulle
 - Hugo Monchablon : idée du nom & soutien moral
 
 Vous souhaitez également participer au développement et à l'amélioration de la norminette ? N'hésitez pas à ouvrir une <i>issue</i> en cas de problème ou à soumettre un <i>pull request</i> pour une idée de modification.
