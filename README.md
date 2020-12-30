[<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/logo.png" width="200px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

Norminette EPITECH développé avec les fonctionnalités de la dernière mise à jour de la norme d'EPITECH pour la promotion 2025. Disponible pour tous les étudiants.
La norminette cherche les erreurs de norme d'Epitech dans le code source des fichiers. La norminette est la plus complète à ce jour et a un système de versioning, permettant les mises à jour régulières.

L'objectif est de garder une norminette complète en moins de 3000 lignes (assets/ exclus).

## Menu

* __[Installation et utilisation](#bubulle)__
  * [Dépendances](#dépendances)
  * [Installation de la norminette](#installation)
  * [Utilisation](#utilisation)
* __[Vérifications de norme](#vérifications-de-norme)__
* __[Options](#options)__
* __[Rapports HTML](#rapports-html)__
* __[Contributeurs](#contributeurs)__

## Bubulle

### Dépendances
  Pour utiliser la norminette Bubulle, vous devez avoir Python 3.x sur votre ordinateur.<br>
  <i>Le script d'installation installe automatiquement les dépendances.</i>
 - [Python](https://python.com)
 - Pycparser : ```python3 -m pip install pycparser pyparsing pycparser-fake-libc --user```<br>
 
La norminette Bubulle utilise un préprocesseur C écrit en Python permettant le fonctionnement de plusieurs tests de norme.

#### Installation

L'installation peut s'effectuer directement avec le script d'installation. Le script supprime l'ancienne version et télécharge la nouvelle. C'est la façon la plus facile d'installer la norminette sous Linux. Fonctionne également sur MacOS.

```
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)"
```

## Utilisation

  Ecrivez simplement la commande suivante dans votre terminal, dans le dossier où se situe le code que vous souhaitez vérifier : 
 `bubulle`
 
 Exemple de retour :

[<img alt="Norminette" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/example1.png" width="570px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

## Vérifications de norme

| ID Norme        | Description           | Géré par Bubulle  |
| ------------- |:-------------:| :-----:|
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O1 | Fichier inutile pour la compilation | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O2 | Fichier source vide | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O3 | Trop de fonctions dans un fichier (> 5 fonctions) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O4 | Nom du fichier pas en <i>snake case</i> | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O4 | Nom du fichier ambigü | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> G1 | Header EPITECH manquant/mal placé dans le fichier | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> G2 | Fonctions devant être séparées par une seule ligne | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> G4 | Variable modifiable en dehors d'une fonction | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F2 | Fonction pas en <i>snake case</i> | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F3 | Ligne trop longue (> 80 caractères) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F4 | Fonction trop longue (> 20 lignes) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F5 | Maximum 4 paramètres par fonction | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F5 | Paramètre 'void' manquant en cas de fonction sans arguments | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> F6 | Commentaires à l'intérieur d'une fonction | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F7 | Fonctions 'nested' | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L1 | Plusieurs assignements sur une même ligne | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L2 | Mauvaise indentation d'une ligne/partie de code | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L2 | Les TABS ne doivent pas être utilisés pour l'indentation | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L3 | Espace manquant après un mot clé | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L3 | Espaces en trop à la fin d'une ligne | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L3 | Espace manquant avant un opérateur/mot clé | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> L4 | Crochets mal positionnés | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L6 | Lignes vides en trop | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> V1 | Nom de variable pas au format <i>snake_case</i> | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> V2 | Les typedef doivent se terminer par <i>_t</i>| <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> V3 | Pointeur mal positionné | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> C1 | Trop de niveaux de code (> 2 niveaux) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> C3 | Mot clé <i>goto</i> interdit | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> H1 | Mauvaise séparation entre fichier source/header | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> H3 | Les macros ne doivent pas être utilisées pour des constantes | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> -42 | Fonctions interdites | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/info.png" width="16" vertical-align="middle"/> T010 | Nom de variable ambigü | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/info.png" width="16" vertical-align="middle"/> F002 | Nom du fichier ou dossier trop long | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/info.png" width="16" vertical-align="middle"/> F002 | Nom du fichier ne commençant pas par une lettre | <font style="color: green; font-size: 16px;">✓</font> |

## Options

 - `-h` ou `--help`: obtenir des informations sur Bubulle (arguments)
 - `-p` ou `--path`: lancer la norminette dans un dossier ou fichier précis
 - `-r` ou `--report`: générer un rapport au format HTML
 - `-e` ou `--exclude`: ignorer un fichier/dossier
 - `-u` ou `--update`: mettre à jour la norminette Bubulle
 - `-c` ou `--config`: afficher/modifier la configuration de Bubulle (expérimental)
 - `-verbose` ou `--verbose`: verbose, afficher les erreurs de compilation <b>précises</b> 
 - `-v` ou `--version`: afficher la version locale de Bubulle 
 - `-ic` ou `--ignore-compilation` : ignorer les erreurs de compilation
 - `-i` ou `--ignore`: ignorer des erreurs de norme précises (séparés par une virgule)<br>
Exemple: <b>l1,l2</b> permet d'ignorer le test L1 et L2
 - `-ii` ou `--ignore-info`: ignorer les problèmes de norme INFO
 - `-imin` ou `--ignore-minor`: ignorer les problèmes de norme MINOR
 - `-imaj` ou `--ignore-major`: ignorer les problèmes de norme MAJOR
 
## Rapports HTML

Bubulle permet de générer un rapport au format HTML (avec `-r` ou `--report`) avec des informations visuelles sur le code et les erreurs de norme directement depuis votre navigateur Internet (ne fonctionne pas en TTy).

<img alt="Rapport HTML" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/example_html_report1.png" style="width: 100%"/>
<br>
<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/example_html_report2.png" style="width: 100%"/>

# Contributeurs
 - aureliancnx : Développeur de la Bubulle
 - Payne : idée du nom & soutien moral
 - toutes les personnes qui testent la norminette et qui me donnent un feedback pour améliorer Bubulle. <3
 
 Vous souhaitez également participer au développement et à l'amélioration de la norminette ? N'hésitez pas à ouvrir une <i>issue</i> en cas de problème ou à soumettre un <i>pull request</i> pour une idée de modification.

-------------------------------------------------------

ENGLISH VERSION

[<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/logo.png" width="200px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

EPITECH norme check developed with the features of the latest update of the EPITECH norme for the 2025 promotion. Available for all students.
The norminette looks for Epitech "norme" errors in the source code of the files. The norminette is the most complete to date and has a versioning system, allowing regular updates.

The goal is to keep a complete norminette in less than 3000 lines (assets/excluded).

## Menu

* __[Install and usage](#bubble)__
  * [Dependencies](#dependencies)
  * [How to install Bubulle?](#installation)
  * [Usage](#use)
* __[Norme verifications](#checks)__
* __[Options (en)](#options)__
* __[HTML Reports](#reports-html)__
* __[Contributors](#contributors)__

## Bubulle

### Dependencies
  In order to use Bubulle, you must have Python 3.x installed.
  The installation script automatically installs the related dependencies.
 - [Python](https://python.com)
 - Pycparser : ```python3 -m pip install pycparser pyparsing pycparser-fake-libc --user```<br>
 
The Bubble norme check uses a C preprocessor written in Python allowing the operation of several standard tests.

#### Installation

The installation can be done directly with the installation script. The script removes the old version and downloads the new one. This is the easiest way to install the norme checker under Linux. Also works on MacOS.

```
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/install_bubulle.sh)"
```

## Usage

  Simply type the following command in your terminal, in the folder where the code you want to check is located: 
 `bubulle`
 
 Output example:

[<img alt="Norme check" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/example1.png" width="570px"/>](https://github.com/aureliancnx/Bubulle-Norminette)

## Checks

| ID Norme        | Description           | Handled by Bubulle?  |
| ------------- |:-------------:| :-----:|
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O1 | Useless file for compilation | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O2 | Empty source file | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O3 | Too many functions in file (> 5 functions) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O4 | File name not in <i>snake case</i> | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> O4 | Ambiguous file name | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> G1 | Missing or misplaced EPITECH header | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> G2 | Functions must be separated by a single line | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> G4 | Editable function outside a function | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F2 | Function not in <i>snake case</i> | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F3 | Too long line (> 80 characters) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F4 | Too long function (> 20 lines) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F5 | More than 4 parameters in a function | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F5 | 'void' parameter is missing if the function is without parameters | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> F6 | Comments inside a function | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> F7 | Nested functions | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L1 | Several assignements in the same line | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L2 | Bad indentation | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L2 | Tabs shouldn't be used for indentation | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L3 | Missing space after a keyword | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L3 | Extra space in line end | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L3 | Missing space before keyword/variable | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> L4 | Misplaced brackets | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> L6 | Useless empty line | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> V1 | Variable name not in <i>snake_case</i> | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> V2 | Typedef should ends with <i>_t</i>| <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> V3 | Misplaced pointer | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> C1 | Too many codes branches (> 2 levels) | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> C3 | Forbidden <i>goto</i> keyword | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> H1 | Bad separation between header/source file | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/minor.png" width="16" vertical-align="middle"/> H3 | Macro should not be used as const | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> -42 | Forbidden functions | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/info.png" width="16" vertical-align="middle"/> T010 | Ambiguous variable name | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/info.png" width="16" vertical-align="middle"/> F002 | Too long file/folder name | <font style="color: green; font-size: 16px;">✓</font> |
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/info.png" width="16" vertical-align="middle"/> F002 | File name should starts with a letter | <font style="color: green; font-size: 16px;">✓</font> |

## Options (en)

 - `-h` or `--help`: get information about Bubble (arguments)
 - `-p` or `--path`: run the norminette in a specific directory or file
 - `-r` or `--report`: generate a report in HTML format
 - `-e` or `--exclude`: ignore a file/folder
 - `-u` or `--update`: update the Bubble Normette
 - `-c` or `--config`: display/modify Bubble configuration (experimental)
 - `-verbose` or `--verbose`: verbose, display compilation errors <b>precise</b> 
 - `-v` or `--version`: display the local version of Bubble 
 - `-ic` or `--ignore-compilation`: ignore compilation errors
 - `-i` or `--ignore`: ignore specific standard errors (comma-separated)<br>
Example: <b>l1,l2</b> ignores the L1 and L2 test.
 - `-ii` or `--ignore-info`: ignore INFO standard problems
 - `-imin` or `--ignore-minor`: ignore MINOR norme issues
 - `-imaj` or `--ignore-major`: ignore MAJOR norme issues
 
## HTML Reports

Bubble allows you to generate a report in HTML format (with `-r` or `--report`) with visual information about the code and norme issues directly from your web browser (does not work in TTy).

<img alt="Rapport HTML" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/example_html_report1.png" style="width: 100%"/>
<br>
<img alt="Norme EPITECH" src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/example_html_report2.png" style="width: 100%"/>

# Contributors
 - aureliancnx : Bubble developer
 - Payne : name idea & moral support
 - all the people who test the norminette and give me feedback to improve Bubble. <3
 
 Would you also like to participate in the development and improvement of norminette? Feel free to open a <i>issue</i> in case of problem or to submit a <i>pull request</i> for a modification idea.
