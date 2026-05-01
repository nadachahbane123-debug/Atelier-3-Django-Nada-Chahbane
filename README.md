# README - Atelier 3 : Authentification avec Django

## 📋 Description

Ce projet est un site e-commerce développé avec **Django**, auquel a été ajouté un **système d'authentification complet** dans le cadre de l'Atelier 3 du module Développement Web avec Python, auquel a été ajouté un **panier d'achat** et la fonctionnalité de **changement de mot de passe**.

L'application `accounts` permet aux utilisateurs de :
- S'inscrire avec un formulaire personnalisé
- Se connecter / se déconnecter
- Accéder à une page profil protégée
- 
L'application `cart` permet aux utilisateurs de :
- Ajouter des produits au panier
- Modifier les quantités
- Supprimer des articles ou vider le panier
- Voir le total et un badge dans la navbar
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
| Ajouter une application `cart` | ✅ |
| Créer les modèles `Cart` et `CartItem` | ✅ |
| Ajouter / retirer / modifier des articles dans le panier | ✅ |
| Afficher le nombre d'articles dans la navbar | ✅ |
| Permettre le changement de mot de passe | ✅ |
| Réutiliser les vues d'authentification intégrées de Django | ✅ |

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
├── cart/                       ← NOUVELLE APPLICATION
│   ├── migrations/
│   ├── templates/
│   │   └── cart/
│   │       └── cart_detail.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── apps.py
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
pip install django pillow psycopg2
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
    'cart',   # Nouvelle application
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
| `/accounts/password_change/` | Changement de mot de passe | `@login_required` |
| `/accounts/password_change/done/` | Confirmation changement | `@login_required` |
| `/cart/` | Voir le panier | `@login_required` |
| `/cart/add/<id>/` | Ajouter un produit | `@login_required` |
| `/cart/remove/<id>/` | Retirer un article | `@login_required` |
| `/cart/update/<id>/` | Modifier la quantité | `@login_required` |
| `/cart/clear/` | Vider le panier | `@login_required` |

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
## Modèles du panier (`cart/models.py`)

```python
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Un panier par utilisateur

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
```
---

## 🛡️ Notions importantes

| Notion | Description |
|--------|-------------|
| **`@login_required`** | Décorateur protégeant les vues (redirection automatique si non connecté) |
| **`{% csrf_token %}`** | Jeton anti-falsification obligatoire dans tout formulaire POST |
| **Hachage des mots de passe** | Django utilise PBKDF2 (jamais de mots de passe en clair) |
| **Sessions** | Maintien de l'utilisateur connecté entre les pages |
| **`get_or_create`** | Crée automatiquement un panier si l'utilisateur n'en a pas |
| **Context processor** | Injecte `cart_item_count` dans tous les templates pour le badge navbar |
| **`password_change`** | Vue intégrée Django, aucune vue custom nécessaire |

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
| `/accounts/password_change/` | ✅ OK |
| `/cart/` (connecté) | ✅ OK |
| `/cart/` (non connecté) | ✅ Redirection vers login |
| `/cart/add/<id>/` | ✅ OK |
| `/admin/` | ✅ OK |

---

##  Difficultés rencontrées et solutions

| Problème | Solution |
|----------|----------|
| `TemplateDoesNotExist` pour `profile.html` | Ajout de `BASE_DIR / 'accounts' / 'templates'` dans `DIRS` |
| Connexion PostgreSQL refusée | Modification de `pg_hba.conf` en mode `trust` |
| Erreur `No such file or directory` pour `manage.py` | Navigation au bon niveau du projet avec `cd` |
| Template `layout.html` vs `base.html` | Adaptation de tous les `{% extends %}` vers `base.html` |
| `touch` et `&&` non reconnus sur PowerShell | Utilisation de `New-Item` à la place |
| Badge panier non affiché dans la navbar | Ajout du context processor dans `settings.py` |
| Templates `password_change` non trouvés | Création manuelle des 2 templates dans `registration/` |

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
- Création d'une application Django avec modèles relationnels
- Utilisation de `get_or_create` pour la gestion du panier
- Création d'un context processor personnalisé
- Utilisation des vues intégrées Django pour le changement de mot de passe
- Gestion des requêtes POST pour modifier des données
- Compréhension du mécanisme de session et de hachage
- Utilisation des URLs d'authentification intégrées
- Affichage conditionnel dans les templates (`{% if user.is_authenticated %}`)
