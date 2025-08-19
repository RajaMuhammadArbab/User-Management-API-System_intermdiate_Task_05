# User Management API

This project provides a Django REST Framework (DRF) based user management system with JWT authentication.  
Features include profile management, password change, and soft delete functionality.

---

##  Setup & Run Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd user_management
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

##  Authentication (JWT)

- Obtain Token:
  ```http
  POST /api/token/
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

- Refresh Token:
  ```http
  POST /api/token/refresh/
  {
    "refresh": "<your_refresh_token>"
  }
  ```

Use the **access token** in the `Authorization` header:
```
Authorization: Bearer <access_token>
```

---

##  API Endpoints

### 1. Register
```http
POST /api/auth/register/
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "TestPass123"
}
```

### 2. Get Profile
```http
GET /api/auth/profile/
Headers: Authorization: Bearer <access_token>

Response:
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com"
}
```

### 3. Update Profile
```http
PUT /api/auth/profile/
Headers: Authorization: Bearer <access_token>
{
  "username": "updateduser",
  "email": "updated@example.com"
}
```

### 4. Change Password
```http
PUT /api/auth/profile/password/
Headers: Authorization: Bearer <access_token>
{
  "old_password": "TestPass123",
  "new_password": "NewPass123"
}
```

### 5. Soft Delete Account
```http
DELETE /api/auth/profile/delete/
Headers: Authorization: Bearer <access_token>

Response:
{
  "message": "Account soft deleted successfully."
}
```

  ### Admin: List Users
```http
GET /api/auth/admin/users/
Authorization: Bearer <admin_access_token>

Response:
[
  {
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "is_active": false
  },
  {
    "id": 2,
    "username": "alice",
    "email": "alice@example.com",
    "is_active": true
  }
]
```

### Admin: Restore Soft Deleted User
```http
PUT /api/auth/admin/users/restore/1/
Authorization: Bearer <admin_access_token>

Responce:
  {
    "id": 2,
    "username": "alice",
    "email": "alice@example.com",
    "is_active": true
  }
```


