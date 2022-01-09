# Diag-plus
Repo pour l'API du projet.
Pour le front-end et back-end, le repo est sur [ce lien](https://github.com/antoine-witkowski/fo-diag-plus)
Projet de 4ème année de Développement Web avec **Python** et **ReactJs**.
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

> - Pour sécuriser Django, il faut isoler la clé secrète créée et les identifiants de votre base de données. Il faudra installer python-environ en ligne de commande.
> - Une fois installé, vous devez créer un .env où vous allez stocker votre clé secrète et les informations de connexion de votre base de données
> Le contenu du .env doit ressembler à la structure dans `.env.example` qui se situe dans le même dossier que `settings.py`

## PostgreSQL et Django

[Voir le fichier DB_Setup.md](DB_Setup.md)

## API

Voir ici : [API](API.md)

## Credits

Daniel-Christian AMBANG

Alexandre TO

Antoine WITKOWSKI
