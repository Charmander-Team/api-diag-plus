# diag-plus

## Mise en place 

Installation de Python sur linux (la commande dépend de la distribution)

```bash
sudo apt-get install python3
```

## Django 

Il faudra installer **pip** pour pouvoir installer Django. L'installation est différente selon les distributions linux.

Il faut ensuite entrer cette commande

```bash
python3 -m pip install Django
```

[Lien de la documentation pour l'introduction sur Django](https://docs.djangoproject.com/en/3.2/intro/contributing/)

N.B = La base du projet a déja été mis en place, faite attention à ce que vous mettez, spécialement pour les identifiants / password de la base de données. (pour l'instant, faudra changer à chaque fois les identifiants dans le fichier `settings.py`).

## Lancer le projet avec Django

Pour pouvoir lancer le serveur local, il faudra se situer dans le dossier diagPlus du projet (attention il y a **2 diagPlus dans le projet**, c'est la structure de Django, il faut se situer dans le premier dossier **diagPlus**).

Une fois dans ce dossier, il faudra lancer la commande

```bash
python3 manager.py runserver
```

Pour le test, normalement ce sera `localhost:8000/hello`. Ca devra afficher un ̀`Hello World` sur la page

### PostgreSQL et Django

Pour utiliser PostgreSQL, il va falloir l'installer avec la commande.

```bash
sudo apt-get install postgres
```

Une fois installé, lancer cette commande : 

```bash
sudo -u postgres createuser --interactive
```

Cette commande va permettre de créer un utilisateur dans Postgres.

De base avec Postgres, tout utilisateur dispose d'une base de données **à son nom**, c'est-à-dire qu'il va essayer de se connecter à une base de données identique au nom d'utilsateur en premier (par défaut). Pour éviter de perdre trop de temps, on va faire comme ça. Entrez cette commande:

```bash
sudo -u postgres createdb votre_username
```

Une fois crée, il faut ajouter l'username avec ceci : 

```bash
sudo adduser votre_username
```

Pour finir, pour avoir accès à votre base de données,

```bash
sudo -i -u votre_username
```

Après avoir créer un modèle dans l'application, il faut générer la migration avec cette commande : 

```bash
python manage.py makemigrations nom_app
```

Pour lancer la migration, utiliser cette commande : 

```bash
python manage.py migrate
```