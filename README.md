# 🗂️ TaskManagerDjangoProject

## 📋 Description

**TaskManagerDjangoProject** est une application web développée avec Django, permettant la gestion de tâches. Elle offre une interface conviviale pour créer, visualiser, modifier et supprimer des tâches, facilitant ainsi l'organisation personnelle ou professionnelle.

## 🚀 Fonctionnalités

- ✅ Création de tâches
- 📄 Liste des tâches
- ✏️ Mise à jour des tâches
- 🗑️ Suppression de tâches
- 💻 Interface utilisateur moderne

## 🛠️ Technologies utilisées

- **Backend** : [Django](https://www.djangoproject.com/) (Python)
- **Frontend** : Angular
- **Base de données** : SQLite (par défaut avec Django)
- **Autres** : [Bootstrap](https://getbootstrap.com/) pour le design réactif

## 📦 Installation
### 1. Cloner le dépôt
```bash
git clone https://github.com/HamCam203/TaskManagerDjangoProject.git
cd TaskManagerDjangoProject
```
### 2. Créer un environnement virtuel
```
python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate
```

### 3. Installer les dépendances
```
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```
python manage.py migrate
```

### 5. Lancer le serveur
```
python manage.py runserver
```
## 📁 Structure du projet
```
TaskManagerDjangoProject/
├── taskmanager/         # Application principale Django
│   ├── migrations/      # Fichiers de migration
│   ├── static/          # Fichiers statiques (CSS, JS, images)
│   ├── templates/       # Templates HTML
│   ├── admin.py         # Interface d'administration
│   ├── apps.py          # Configuration de l'application
│   ├── models.py        # Modèles de données
│   ├── tests.py         # Tests unitaires
│   └── views.py         # Logique de présentation
├── manage.py            # Script de gestion Django
├── requirements.txt     # Dépendances Python
└── README.md            # Ce fichier
```
