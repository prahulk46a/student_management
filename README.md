# 🚀 Django Project Setup (Production-Oriented Cheat Sheet)

## 1. Project Creation

```bash
django-admin startproject config
cd config
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install django djangorestframework

mkdir apps
cd apps
django-admin startapp student_management
cd ..
```

---

## 2. Recommended Folder Structure

```
config/
apps/
 └── student_management/
      ├── models/
      ├── serializers/
      ├── services/
      ├── views/
      ├── urls/
```

---

## 3. Settings Configuration

```python
INSTALLED_APPS = [
    'rest_framework',
    'apps.student_management.apps.StudentManagementConfig',
]
```

```python
# apps.py
name = 'apps.student_management'
```

---

## 4. URL Configuration

```python
from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.student_management.urls.student_urls')),
]
```

⚠️ Always import `include` from `django.urls`

---

## 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Model Import Rules

❌ Wrong:

```python
from apps.student_management.models import student_model
```

✅ Correct:

```python
from apps.student_management.models.student_model import Student
```

Optional:

```python
# models/__init__.py
from .student_model import Student
```

---

## 7. View Strategy

* Function-based → quick testing
* APIView → controlled logic
* ViewSet → ✅ production-ready

---

## 8. Pagination & Filtering

```
GET /api/students/?page=1&size=10&name=rahul
```

👉 Prefer DRF pagination classes in production

---

## 9. Permissions

If using:

```python
DjangoModelPermissions
```

Then:

```python
queryset = Model.objects.all()
```

---

## 10. Common Mistakes

* Wrong imports (e.g., XML include)
* Incorrect AppConfig path
* Circular URL includes
* Missing `__init__.py`
* No migrations
* Fat views (business logic inside views)
* Importing module instead of class

---

## 11. Production Mindset

* Thin views
* Service layer
* Modular structure
* Reusable components

---

## 12. Minimum Production Checklist

* ✔ Modular architecture
* ✔ .env configs
* ✔ DRF setup
* ✔ Pagination
* ✔ Error handling
* ✔ Logging
* ✔ Clean imports

---

## 💡 Key Rule

Think scalability, not just “working API”
