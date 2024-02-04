# Tool Box Crypto

Il s'agit d'une application Python qui propose une interface utilisateur utilisant un système d'authentification,et la possibilité de chiffrer/déchiffrer des fichiers à l'aide de différents algorithmes cryptographiques.

## Fonctionnalités

- **Authentification des utilisateurs :** Permet aux utilisateurs de s'inscrire avec un nom d'utilisateur et un mot de passe, et de se connecter de manière sécurisée.

- **Stockage des mots de passe :** Hashes et stocke les mots de passe en utilisant l'algorithme PBKDF2.

- **Chriffrement/Déchiffrement de fichiers :** Prend en charge les algorithmes de chiffrements symétriques (AES, DES), asymétrique (RSA) et hybride (RSA / AES).

## Premiers Pas

### Prérequis

- Python 3.x
- Packages Python supplémentaires (à installer avec `pip install -r requirements.txt`) :
  - `customtkinter`
  - `ttkthemes`
  - `cryptography`
  - `passlib`
  - `Crypto`

### Installation

1. Clonez le dépôt : `git clone https://github.com/lilrjh/cryptographie`
2. Accédez au répertoire du projet : `cd cryptographie`
3. Installez les dépendances requises : `pip install -r requirements.txt`

### Utilisation

1. Exécutez l'application : `python ToolBox_Crypto.py`
2. Suivez les instructions pour vous inscrire ou vous connecter.
3. Choisissez les options de chiffrement ou de déchiffrement en fonction de vos besoins.

## Contribution

Si vous souhaitez contribuer à ce projet, n'hésitez pas à cloner le dépôt et à soumettre une pull request.

## Créateurs
Lilian, Baptiste et Titouan dans le cadre d'un projet de cryptographie en Bachelor 3.
