# Diag-plus
Repo pour l'API du projet.
Pour le front-end et back-end, le repo est sur [ce lien](https://github.com/antoine-witkowski/fo-diag-plus)
Projet de 4ème année de Développement Web avec **Python** et **ReactJs**.
## Mise en place 

Installation de Python sur linux (la commande dépend de la distribution)

```bash
sudo apt-get install python3
```

## Pré requis

Pour lancer ce projet, il est **conseillé** de travailler dans un environnement virtuel de Python. Cela va isoler les packages Python et les installer dans un dossier à part qui sera utilisé que dans l'environnement virtuel. Il existe plusieurs packages pour cela dont `virtualenv`  clet `pipenv`.

Avec `virtualenv`, il va falloir entrer la commande qui va permettre de créer un environnement virtuel.

```bash
virtualenv -p python3 envname
# Exemple : virtualenv -p python3 projet
```

Pour ensuite activer cet environnement, il faut entrer cette commande : 
```bash
source cheminversenv/envname/bin/activate
# source ~/.virtualenvs/projet/bin/activate
```
## Django

Il faudra installer **pip** pour pouvoir installer Django. L'installation est différente selon les distributions linux.

Il faut ensuite entrer cette commande

```bash
python3 -m pip install Django
```
Les packages du projet sont stockées dans le fichier `requirements.txt` et pour installer ces packages, vous devez entrer cette commande :

```bash
pip install -r requirements.txt
```

[Lien de la documentation pour l'introduction sur Django](https://docs.djangoproject.com/en/3.2/intro/contributing/)
## Lancer le projet avec Django

Pour pouvoir lancer le serveur local, il faudra se situer dans le dossier diagPlus du projet (attention il y a **2 diagPlus dans le projet**, c'est la structure de Django, il faut se situer dans le premier dossier **diagPlus**).

Une fois dans ce dossier, il faudra lancer la commande

```bash
python3 manage.py runserver
```

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
