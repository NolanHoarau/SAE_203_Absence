# Déploiement Django + Gunicorn + Nginx avec MariaDB distante (Debian 12)

## Infrastructure
- **Server-web (Django + Gunicorn + Nginx)** : `192.168.66.230`
- **Server-DB (MariaDB)** : `192.168.66.70`

---

## 1. Serveur MariaDB (Serveur-DB)

### Installer MariaDB
```bash
sudo apt update
sudo apt install mariadb-server
```

### Créer la base et l'utilisateur
```sql
sudo mariadb
```

Puis j'ai importer le fichier .sql

```bash
mysql -u root -p nom_de_la_base < /home/toto/gestion_absences.sql
```

```sql
CREATE USER 'admin'@'192.168.66.230' IDENTIFIED BY 'toto';
GRANT ALL PRIVILEGES ON myproject.* TO 'admin'@'192.168.66.230';
FLUSH PRIVILEGES;
EXIT;
```
### Autoriser les connexions distantes
```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```
Modifier :
```ini
bind-address = 0.0.0.0
```

Redémarrer le service :
```bash
sudo systemctl restart mariadb
```

---

## 2. Serveur Django (Server-web)

### Installer les paquets nécessaires
```bash
sudo apt update
sudo apt install python3-pip python3-dev libmariadb-dev build-essential libssl-dev libffi-dev python3-venv
```

### Préparer le projet

Importation de l'application django dans /home/toto

```bash
cd ~/gestion_absences
python3 -m venv venv
source venv/bin/activate
```

### Installer Django et les dépendances
```bash
(.venv) pip install django gunicorn mysqlclient
```
Si erreur pour `mysqlclient` :  
```bash
sudo apt install default-libmysqlclient-dev
```

### Configurer `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'django_user',
        'PASSWORD': 'your_password',
        'HOST': '192.168.6.70',
        'PORT': '3306',
    }
}

ALLOWED_HOSTS = ['192.168.66.230']
```

### Migrer la base de données
```bash
(.venv) python manage.py migrate
```

---

## 3. Gunicorn

### Tester Gunicorn
```bash
gunicorn --workers 3 --bind 127.0.0.1:8000 myproject.wsgi:application
```

### Créer le service systemd
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Contenu :
```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/home/your_username/gestion_absences
ExecStart=/home/toto/gestion_absences/.venv/bin/gunicorn --workers 3 --bind unix:/home/toto/gestion_absences/gestion_absences.sock gestion_absences.wsgi:application

[Install]
WantedBy=multi-user.target
```

Puis :
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

---

## 4. Nginx

### Installer Nginx
```bash
sudo apt install nginx
```

### Créer la configuration du site
```bash
sudo nano /etc/nginx/sites-available/gestion_absences
```

Contenu :
```nginx
server {
    listen 80;
    server_name 192.168.66.230;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/toto/gestion_abences;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/toto/gestion_absences/gestion_absences.sock;
    }
}
```

### Activer et redémarrer Nginx
```bash
sudo ln -s /etc/nginx/sites-available/gestion_absences /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

---

## Test final

Ouvre ton navigateur sur :  
```
http://192.168.66.230
```

Notre application Django s'affiche et est fonctionnel