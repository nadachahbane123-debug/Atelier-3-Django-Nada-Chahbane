# README - Atelier 3 : Authentification avec Django

## 📋 Description

Ce projet est un site e-commerce développé avec **Django**, auquel a été ajouté un **système d'authentification complet** dans le cadre de l'Atelier 3 du module Développement Web avec Python.

L'application `accounts` permet aux utilisateurs de :
- S'inscrire avec un formulaire personnalisé
- Se connecter / se déconnecter
- Accéder à une page profil protégée

---

## 🎯 Objectifs de l'atelier

| Objectif | Statut |
|----------|--------|
| Ajouter une application `accounts` | ✅ |
| Utiliser le système d'authentification intégré de Django | ✅ |
| Créer une page d'inscription avec formulaire personnalisé | ✅ |
| Créer une page de connexion | ✅ |
| Gérer la déconnexion | ✅ |
| Créer une page profil protégée (`@login_required`) | ✅ |
| Réutiliser le template `base.html` existant | ✅ |

---

## 🏗️ Architecture du projet

```
ecommerce/
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── products/
│   ├── templates/
│   │   ├── base.html
│   │   ├── product_list.html
│   │   └── product_detail.html
│   ├── urls.py
│   └── views.py
├── accounts/               ← NOUVELLE APPLICATION
│   ├── templates/
│   │   └── registration/
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── profile.html
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── myenv/
```

---

## 🔧 Installation et configuration

### 1. Cloner le projet
```bash
git clone <repository-url>
cd ecommerce
```

### 2. Créer et activer un environnement virtuel
```bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# Mac/Linux
source myenv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install django
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Créer un superutilisateur (optionnel)
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

---

## 🔑 Configuration clé (`settings.py`)

```python
INSTALLED_APPS = [
    ...,
    'products',
    'accounts',           # Nouvelle application
]

# Redirections d'authentification
LOGIN_REDIRECT_URL = "profile"      # Après connexion
LOGOUT_REDIRECT_URL = "product_list" # Après déconnexion
LOGIN_URL = "login"                  # Page de connexion

# Templates
TEMPLATES = [{
    'DIRS': [BASE_DIR / 'accounts' / 'templates'],
    ...
}]
```

---

## 🌐 URLs disponibles

| URL | Description | Protection |
|-----|-------------|------------|
| `/` | Redirection vers liste des produits | - |
| `/products/` | Liste des produits | - |
| `/accounts/signup/` | Inscription | - |
| `/accounts/login/` | Connexion | - |
| `/accounts/logout/` | Déconnexion | - |
| `/accounts/profile/` | Profil utilisateur | `@login_required` |
| `/admin/` | Administration Django | Superutilisateur |

---

## 📝 Formulaires personnalisés

### `accounts/forms.py`
```python
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
```

---

## 🛡️ Notions importantes

| Notion | Description |
|--------|-------------|
| **`@login_required`** | Décorateur protégeant les vues (redirection automatique si non connecté) |
| **`{% csrf_token %}`** | Jeton anti-falsification obligatoire dans tout formulaire POST |
| **Hachage des mots de passe** | Django utilise PBKDF2 (jamais de mots de passe en clair) |
| **Sessions** | Maintien de l'utilisateur connecté entre les pages |

---

## 🧪 Tests effectués

| URL | Résultat |
|-----|----------|
| `/products/` | ✅ OK |
| `/accounts/signup/` | ✅ OK |
| `/accounts/login/` | ✅ OK |
| `/accounts/profile/` (connecté) | ✅ OK |
| `/accounts/profile/` (non connecté) | ✅ Redirection vers login |
| `/accounts/logout/` | ✅ OK |
| `/admin/` | ✅ OK |

---

## 🐛 Difficultés rencontrées et solutions

| Problème | Solution |
|----------|----------|
| `TemplateDoesNotExist` pour `profile.html` | Ajout de `BASE_DIR / 'accounts' / 'templates'` dans `DIRS` |
| Connexion PostgreSQL refusée | Modification de `pg_hba.conf` en mode `trust` |
| Erreur `No such file or directory` pour `manage.py` | Navigation au bon niveau du projet avec `cd` |
| Template `layout.html` vs `base.html` | Adaptation de tous les `{% extends %}` vers `base.html` |

---

## 👤 Auteur

**Nada Chahbane**  
École Mohammadia d'Ingénieurs - Rabat  
Année Universitaire : 2025-2026  
Professeur : Mr. A. BOUSSELHAM

---

## 📚 Compétences acquises

- Création et intégration d'une application Django
- Utilisation de `UserCreationForm` personnalisé
- Protection de vues avec `@login_required`
- Compréhension du mécanisme de session et de hachage
- Utilisation des URLs d'authentification intégrées
- Affichage conditionnel dans les templates (`{% if user.is_authenticated %}`)
