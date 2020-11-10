[<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/images/logo.png" width="200px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

Norminette EPITECH développé avec les fonctionnalités de la dernière mise à jour de la norme d'EPITECH pour la promotion 2025. Disponible pour tous les étudiants.
La norminette cherche les erreurs de norme d'Epitech dans le code source des fichiers. La norminette est la plus complète à ce jour et a un système de versioning, permettant les mises à jour régulières.

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
  Pour utiliser la norminette Bubulle, vous devez avoir Python 3.x et pycparser installé sur votre ordinateur.<br>
  <i>Le script d'installation installe automatiquement les dépendances.</i>
 - [Python](https://python.com)
 - Pycparser : ```pip install pycparser pyparsing --user```<br>
 
La norminette Bubulle utilise un préprocesseur C écrit en Python permettant le fonctionnement de plusieurs tests de norme.

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

 - `-h` ou `--help`: obtenir des informations sur Bubulle (arguments)
 - `-p` ou `--path`: lancer la norminette dans un dossier ou fichier précis
 - `-r` ou `--report`: générer un rapport au format HTML
 - `-e` ou `--exclude`: ignorer un fichier/dossier
 - `-u` ou `--update`: mettre à jour la norminette Bubulle
 - `-v` ou `--verbose`: verbose, afficher les erreurs de compilation <b>précises</b> 
 - `-ic` ou `--ignore-compilation` : ignorer les erreurs de compilation du préprocesseur
 - `-i` ou `--ignore`: ignorer des erreurs de norme précises (séparés par une virgule)<br>
Exemple: <b>l1,l2</b> permet d'ignorer le test L1 et L2
 - `-ii` ou `--ignore-info`: ignorer les problèmes de norme INFO
 - `-imin` ou `--ignore-minor`: ignorer les problèmes de norme MINOR
 - `-imaj` ou `--ignore-major`: ignorer les problèmes de norme MAJOR
 
## Rapports HTML

Bubulle permet de générer un rapport au format HTML (avec `-r` ou `--report`) avec des informations visuelles sur le code et les erreurs de norme directement depuis votre navigateur Internet (ne fonctionne pas en TTy).

<img alt="Rapport HTML" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/images/example_html_report1.png" width="300px"/>
<br>
<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/images/example_html_report2.png" width="300px"/>
 
## Fonctionnalités

### Vérification des fichiers
 - Vérification des fichiers qui ne sont pas en accord avec la convention snake_case
 - Vérification des fichiers sources qui n'ont pas pour extension .c ni .h
 - Vérification des fichiers inutiles
 - Vérification des fichiers sources vides
 - Vérification des noms de fichiers qui ne sont pas clairs (par exemple: test.c, string.c ...)
 - Verification des erreurs de compilation des fichiers sources, afin de s'en rendre compte avant d'avoir un 0.

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
 - Détection des fonctions qui ne possèdent pas de paramètre (ni de "void" par convention)
 - Vérification de l'indentation : les tabs sont interdits, ils doivent être remplacés par quatre espaces.
 - Détection des lignes en trop (deux lignes ou plus vides par exemple)
 - Détection des macros utilisées pour des constantes : elles doivent servir pour remplacer des fonctions en une ligne
 - Détection des espaces manquants entre les virgules
 - Détection des assignements de variables multiples sur une seule et même ligne
 - Détection des commentaires dans les fonctions
 - Détection des nested fonctions
 - Vérification de l'indentation complète de chaque ligne

# Contributeurs
 - aureliancnx : Développeur de la Bubulle
 - Payne : idée du nom & soutien moral
 - toutes les personnes qui testent la norminette et qui me donnent un feedback pour améliorer Bubulle. <3
 
 Vous souhaitez également participer au développement et à l'amélioration de la norminette ? N'hésitez pas à ouvrir une <i>issue</i> en cas de problème ou à soumettre un <i>pull request</i> pour une idée de modification.
