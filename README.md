# 🚀 Django Student Management System

A comprehensive Django REST API project demonstrating advanced model relationships, CRUD operations, and production-ready architecture for managing students, teachers, courses, and subjects.

## 📋 Project Overview

This project implements a multi-level mapping system where:
- Students can enroll in multiple courses
- Teachers can teach multiple subjects
- Teachers can teach multiple students
- Courses can have multiple subjects

Built with Django REST Framework, featuring modular architecture, many-to-many relationships, and scalable API design.

## ✨ Features

### Core Functionality
- **Full CRUD Operations** for all entities (Students, Teachers, Courses, Subjects)
- **Many-to-Many Relationships** management
- **Pagination & Filtering** for efficient data retrieval
- **RESTful API Design** with proper HTTP methods
- **Django Admin Integration** for easy data management

### Advanced Features
- **Relationship Management APIs** (enroll/unenroll, assign/remove)
- **Nested Serialization** for complex data structures
- **Modular Architecture** with separated concerns
- **Production-Ready Structure** following Django best practices

## 🏗️ Project Structure

```
config/
├── db.sqlite3
├── manage.py
├── README.md
├── apps/
│   └── student_management/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── student_model.py
│       ├── serializers/
│       │   ├── __init__.py
│       │   ├── student_serializer.py
│       │   ├── subject_serializer.py
│       │   ├── course_serializer.py
│       │   └── teacher_serializer.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── student_service.py
│       ├── urls/
│       │   ├── __init__.py
│       │   ├── student_urls.py
│       │   ├── subject_urls.py
│       │   ├── course_urls.py
│       │   └── teacher_urls.py
│       ├── views/
│       │   ├── __init__.py
│       │   ├── student_view.py
│       │   ├── subject_view.py
│       │   ├── course_view.py
│       │   └── teacher_view.py
│       └── migrations/
│           ├── __init__.py
│           └── 0002_course_subject_student_courses_course_subjects_and_more.py
└── config/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 📊 Models & Relationships

### Entity Models

#### Student
- `name` (CharField)
- `age` (IntegerField)
- `email` (EmailField, unique)
- `courses` (ManyToManyField to Course)
- `created_at` (DateTimeField)

#### Teacher
- `name` (CharField)
- `email` (EmailField, unique)
- `subjects` (ManyToManyField to Subject)
- `students` (ManyToManyField to Student)
- `created_at` (DateTimeField)

#### Course
- `name` (CharField)
- `description` (TextField)
- `subjects` (ManyToManyField to Subject)
- `created_at` (DateTimeField)

#### Subject
- `name` (CharField)
- `description` (TextField)
- `created_at` (DateTimeField)

### Relationship Diagram

```
Student ────┼─── Course
     │      │
     │      │
     ▼      ▼
Teacher ────┼─── Subject
```

- **Student ↔ Course**: Many-to-many (enrollment)
- **Teacher ↔ Subject**: Many-to-many (teaching subjects)
- **Teacher ↔ Student**: Many-to-many (teaching students)
- **Course ↔ Subject**: Many-to-many (course subjects)

## 🔗 API Endpoints

### Students API
- `GET /api/students/` - List students (pagination: `?page=1&size=5&name=filter`)
- `POST /api/students/create/` - Create new student
- `GET /api/students/<id>/` - Get student details
- `PUT /api/students/update/<id>/` - Update student
- `DELETE /api/students/delete/<id>/` - Delete student
- `POST /api/students/<student_id>/enroll/<course_id>/` - Enroll student in course
- `DELETE /api/students/<student_id>/unenroll/<course_id>/` - Unenroll student from course

### Teachers API
- `GET /api/teachers/` - List teachers
- `POST /api/teachers/create/` - Create new teacher
- `GET /api/teachers/<id>/` - Get teacher details
- `PUT /api/teachers/update/<id>/` - Update teacher
- `DELETE /api/teachers/delete/<id>/` - Delete teacher
- `POST /api/teachers/<teacher_id>/assign-subject/<subject_id>/` - Assign subject to teacher
- `DELETE /api/teachers/<teacher_id>/remove-subject/<subject_id>/` - Remove subject from teacher
- `POST /api/teachers/<teacher_id>/assign-student/<student_id>/` - Assign student to teacher
- `DELETE /api/teachers/<teacher_id>/remove-student/<student_id>/` - Remove student from teacher

### Courses API
- `GET /api/courses/` - List courses
- `POST /api/courses/create/` - Create new course
- `GET /api/courses/<id>/` - Get course details
- `PUT /api/courses/update/<id>/` - Update course
- `DELETE /api/courses/delete/<id>/` - Delete course

### Subjects API
- `GET /api/subjects/` - List subjects
- `POST /api/subjects/create/` - Create new subject
- `GET /api/subjects/<id>/` - Get subject details
- `PUT /api/subjects/update/<id>/` - Update subject
- `DELETE /api/subjects/delete/<id>/` - Delete subject

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- Virtual environment

### Installation

1. **Clone/Create Project**
   ```bash
   cd "D:\PersonalFolder\PersonalProjects\Python learnings"
   # Project is already set up in config/
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access APIs**
   - API Base: `http://localhost:8000/api/`
   - Admin Panel: `http://localhost:8000/admin/`

## 📝 Usage Examples

### Create a Subject
```bash
curl -X POST http://localhost:8000/api/subjects/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Mathematics", "description": "Advanced Mathematics"}'
```

### Create a Student
```bash
curl -X POST http://localhost:8000/api/students/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "age": 20, "email": "john@example.com"}'
```

### Enroll Student in Course
```bash
curl -X POST http://localhost:8000/api/students/1/enroll/1/
```

### Get Students with Pagination
```bash
curl "http://localhost:8000/api/students/?page=1&size=5&name=john"
```

## 🎓 Main Learnings from This Project

### 1. **Django Model Relationships**
- Understanding Many-to-Many relationships and their implementation
- Using `related_name` for reverse relationships
- Proper model design for complex business logic

### 2. **REST API Design**
- Building RESTful endpoints with proper HTTP methods
- Nested resource URLs for relationship management
- Consistent API patterns across entities

### 3. **Serialization Best Practices**
- Nested serializers for complex data structures
- Write-only fields for relationship management
- Handling many-to-many relationships in serializers

### 4. **Modular Architecture**
- Separating concerns (models, views, serializers, services)
- URL modularization for maintainability
- Reusable components across the application

### 5. **Django Admin Integration**
- Registering models with admin for easy data management
- Understanding admin's automatic relationship handling

### 6. **Migration Management**
- Creating and applying migrations for schema changes
- Handling complex relationship migrations
- Database evolution best practices

### 7. **Production-Ready Patterns**
- Thin views with business logic in services
- Proper error handling and status codes
- Scalable URL configurations

### 8. **Common Pitfalls Avoided**
- Circular imports in complex relationships
- Improper URL includes causing conflicts
- Fat views with mixed responsibilities
- Inconsistent API naming conventions

## 🛠️ Production Checklist

- ✅ **Modular Architecture** - Separated apps and concerns
- ✅ **REST Framework Setup** - DRF for API development
- ✅ **Pagination & Filtering** - Efficient data retrieval
- ✅ **Error Handling** - Proper HTTP status codes
- ✅ **Clean Imports** - Correct module importing
- ✅ **Migrations Applied** - Database schema ready
- ✅ **Admin Integration** - Easy data management
- ✅ **Relationship Management** - Complex mappings handled

## 💡 Key Takeaways

1. **Think Relationships First** - Design models with relationships in mind
2. **Modular URLs** - Separate URL files for maintainability
3. **Service Layer** - Keep business logic out of views
4. **Consistent API Design** - Follow REST principles
5. **Test Relationships** - Many-to-many operations need careful testing
6. **Admin is Your Friend** - Use Django admin for data verification
7. **Migrations Matter** - Always apply and version control migrations

## 🔄 Future Enhancements

- Add authentication and permissions
- Implement advanced filtering and search
- Add data validation and constraints
- Include API documentation (Swagger/OpenAPI)
- Add unit and integration tests
- Implement caching for performance
- Add logging and monitoring

---

**Built with ❤️ using Django REST Framework**

*Focus on scalability, maintainability, and clean architecture from day one!*
