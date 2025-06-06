## Configuration VM

- Installation de deux  Machine Virtuelle Debian sans interfaces graphique en NA\T

### Installation des paquets nécessaire au bon fonctionnement du serveur

```bash
$ sudo apt update

$ sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
- `python3-venv` -> environnement virtuel python
- `python3-dev` -> Pour Guinicorn (plus loin)
- `libpq-dev` -> pour se connecter a un serveur PostgreSQL
- `postgresql` / `postgresql-contrib` -> serveur PostgreSQL pour les base de données relationnelle
- `nginx` -> serveur web comme apache (mais en mieux)
- `curl` ->  permettant de faire des requêtes HTTP

### Creation de l'utilisateur PostgreSQL

PostgreSQL c'est un systeme e base de donnees relationnel (DBRM) equivalent de MySQL

```bash
$ sudo -u postgres psql
```

Cette commande permet de me connecter au terminal PostgreSQL (`psql`) en tant qu'utilisateur système `postgres` qui est le super-utilisateur par défaut de la base de données PostgreSQL, ce qui permet :

- d’administrer les bases de données PostgreSQL,
- de créer des utilisateurs, bases, rôles, ...
- d’exécuter des requêtes SQL avec les droits d’admin.

### DB pour le projet

une fois connecter au terminal `psql`
`postgres=#`
```sql
CREATE DATABASE gestion_absences;
CREATE USER gestion_absences_user WITH PASSWORD 'toto';
```

