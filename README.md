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
## Lancer le projet avec Django

Pour pouvoir lancer le serveur local, il faudra se situer dans le dossier diagPlus du projet (attention il y a **2 diagPlus dans le projet**, c'est la structure de Django, il faut se situer dans le premier dossier **diagPlus**).

Une fois dans ce dossier, il faudra lancer la commande

```bash
python3 manager.py runserver
```

Pour le test, normalement ce sera `localhost:8000/hello`. Ca devra afficher un ̀`Hello World` sur la page