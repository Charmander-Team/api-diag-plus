# PostgreSQL et Django

Pour utiliser PostgreSQL, il va falloir l'installer avec la commande. (Depend de votre distribution linux)

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
psql db_name username
```

Après avoir créer un modèle dans l'application, il faut générer la migration avec cette commande : 

```bash
python manage.py makemigrations nom_app
```

Pour lancer la migration, utiliser cette commande : 

```bash
python manage.py migrate
```
