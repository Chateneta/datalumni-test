# Datalumni - coding tests
## Test Javascript
### Règles du jeu
- Vous utiliserez [CodeSandbox](https://codesandbox.io/) pour produire votre projet
- Vous utiliserez uniquement du **Javascript vanilla** et **Vue.js**
- La seule dépendance autorisée est `axios` ([CDN ici](https://cdnjs.com/libraries/axios), ou directement via les dépendances dans votre projet)
- Vous considérerez que l'utilisateur utilise un navigateur moderne et à jour
- Pas de prérequis pour le rendu esthétique, vous utiliserez votre framework CSS préféré

### Livrable attendu
Pour cet exercice, il vous est demandé de faire un fork de ce [projet CodeSandbox](https://codesandbox.io/s/datalumni-test-template-b1fe7). Ce fork contiendra l'ensemble de votre code.

Vous devez créer une app affichant une liste d'utilisateurs. Les informations proviennent d'une app fictive et sont rendues disponibles à travers une API REST.

L'application contient les fonctionnalités suivantes :
- Les données relatives aux utilisateurs sont récupérables [via une API REST](https://randomuser.me/)
- L'app est divisée en deux composant : la **liste des utilisateurs** et **le profil détaillé**
- Liste des utilisateurs :
    - La liste est composée de 10 utilisateurs
    - Les utilisateurs sont listés par leur `Prénom NOM`
    - Lorsqu'on clique sur un utilisateur, sont profil détaillé s'affiche
    - L'utilisateur actif (sélectionné) apparaît en survrillance dans la liste
    - Un bouton `Ajouter un utilisateur` est présent au bas de la liste et ajoute un nouvel utilisateur dans la liste (les données de cet utilisateur sont récupérées [via l'API REST](https://randomuser.me/))
- Profil utilisateur détaillé
    - Si aucun utilisateur n'est sélectionné, un message nous invite à cliquer sur le nom d'un utilisateur dans la liste
    - Le profil détaillé affiche les informations suivantes :
        - `Photo`
        - `Civilité`, `Prénom`, `Nom`
        - `Nationalité`
        - `Date de naissance`
        - `Ville`
        - `Pays`
        - `Email`
        - `Téléphone`
        - `Mobile`
        - `Username`
        - `UUID`
    - Deux boutons d'action sont présents dans le profil :
        - `Dupliquer l'utilisateur` : Crée une copie de l'utilisateur dans la liste (avec la mention `(copie)` à côté de sont nom) et le sélectionne
        - `Supprimer l'utilisateur` : Supprime l'utilisateur de la liste et le désélectionne
        - Remarque : aucune action (`POST`, `DELETE`) ne doit être faite sur l'API pour ces deux boutons. Seule la liste déjà récupérée (et en mémoire) sera modifiée


#### Exemple de rendu
![Exemple datalumni-test-vue](https://github.com/waldeck-dev/datalumni-test/blob/master/javascript/datalumni-test-vue2.png?raw=true)

---

## Test Python
### Règles du jeu
- Vous utiliserez Python 3.7+
- Vous n'utiliserez pas de modules tiers, seulement les modules Python natifs

### Livrables attendus
#### livrable n°1
Pour cet exercice, il vous est demandé de compléter le fichier `python/number.py`.

Vous recherchez un nombre en 1 et 1000. Un seul nombre nombre correspond à la description suivante :
- Le nombre est composé de deux chiffres ou plus
- Le nombre ne contient pas de 1, ni de 7
- La somme de ses chiffres est inférieure ou égale 10
- Les deux premiers chiffres donne un nombre impair quand on les additionne
- L'avant dernier chiffre est un 4
- Le dernier chiffre est égal au nombre de chiffre composant le nombre

#### livrable n°2
Pour cet exercice, il vous est demandé de compléter le fichier `python/student.py`. Les consignes concernant les différents scripts à produire sont notés en commentaire dans ce fichier.

---

## Livraison
Pour livrer votre travail :
- Vous effectuerez un fork de ce repository [`waldeck-dev/datalumni-test`](https://github.com/waldeck-dev/datalumni-test)
- Vous nous transmettrez le lien vers votre repository contenant votre travail
- Vous renseignerez le lien vers votre projet CodeSandbox

#### Lien vers votre CodeSandbox
```
URL : https://codesandbox.io/s/fancy-cdn-2bett
```