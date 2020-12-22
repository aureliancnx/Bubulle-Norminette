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
| <img src="https://raw.githubusercontent.com/aureliancnx/Bubulle-Norminette/master/assets/images/major.png" width="16" vertical-align="middle"/> H1 | Mauvaise séparation entre fichier source/header | <font style="color: green; font-size: 16px;">TODO</font> |
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
