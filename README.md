

```markdown
# README - Atelier 3 : Django ecommerce project

## 📋 Description

Ce projet est un site e-commerce développé avec **Django**, auquel a été ajouté un **panier d'achat** et la fonctionnalité de **changement de mot de passe** dans le cadre de l'Atelier 4 du module Développement Web avec Python.

---

## 🎯 Objectifs de l'atelier

| Objectif | Statut |
|----------|--------|
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
├── accounts/
│   ├── templates/
│   │   └── registration/
│   │       ├── login.html
│   │       ├── signup.html
│   │       ├── profile.html
│   │       ├── password_change_form.html    ← NOUVEAU
│   │       └── password_change_done.html    ← NOUVEAU
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
    'accounts',
    'cart',           # Nouvelle application
]

TEMPLATES = [{
    'OPTIONS': {
        'context_processors': [
            ...
            'cart.context_processors.cart_count',  # Badge panier navbar
        ],
    },
}]

LOGIN_REDIRECT_URL = "profile"
LOGOUT_REDIRECT_URL = "product_list"
LOGIN_URL = "login"
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
| `/accounts/password_change/` | Changement de mot de passe | `@login_required` |
| `/accounts/password_change/done/` | Confirmation changement | `@login_required` |
| `/cart/` | Voir le panier | `@login_required` |
| `/cart/add/<id>/` | Ajouter un produit | `@login_required` |
| `/cart/remove/<id>/` | Retirer un article | `@login_required` |
| `/cart/update/<id>/` | Modifier la quantité | `@login_required` |
| `/cart/clear/` | Vider le panier | `@login_required` |
| `/admin/` | Administration Django | Superutilisateur |

---

## 🛒 Modèles du panier (`cart/models.py`)

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
| **`@login_required`** | Toutes les vues du panier sont protégées |
| **`get_or_create`** | Crée automatiquement un panier si l'utilisateur n'en a pas |
| **Context processor** | Injecte `cart_item_count` dans tous les templates pour le badge navbar |
| **`password_change`** | Vue intégrée Django, aucune vue custom nécessaire |

---

## 🧪 Tests effectués

| URL | Résultat |
|-----|----------|
| `/cart/` (connecté) | ✅ OK |
| `/cart/` (non connecté) | ✅ Redirection vers login |
| `/cart/add/<id>/` | ✅ OK |
| `/cart/update/<id>/` | ✅ OK |
| `/cart/remove/<id>/` | ✅ OK |
| `/cart/clear/` | ✅ OK |
| `/accounts/password_change/` | ✅ OK |
| `/accounts/password_change/done/` | ✅ OK |

---

## 🐛 Difficultés rencontrées et solutions

| Problème | Solution |
|----------|----------|
| `touch` et `&&` non reconnus sur PowerShell | Utilisation de `New-Item` à la place |
| Badge panier non affiché dans la navbar | Ajout du context processor `cart.context_processors.cart_count` dans `settings.py` |
| Templates `password_change` non trouvés | Création manuelle de `password_change_form.html` et `password_change_done.html` |

---

## 👤 Auteur

**Nada Chahbane**  
École Mohammadia d'Ingénieurs - Rabat  
Année Universitaire : 2025-2026  
Professeur : Mr. A. BOUSSELHAM

---

## 📚 Compétences acquises

- Création d'une application Django avec modèles relationnels
- Utilisation de `get_or_create` pour la gestion du panier
- Création d'un context processor personnalisé
- Utilisation des vues d'authentification intégrées pour le changement de mot de passe
- Gestion des requêtes POST pour modifier des données
```
