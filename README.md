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

## Project-Demo ##
<img width="1357" height="687" alt="3" src="https://github.com/user-attachments/assets/1a8c4b8c-414e-41cf-ba21-7d520d789ef5" />
<img width="1389" height="657" alt="4" src="https://github.com/user-attachments/assets/062223a2-f211-4d5a-bd2a-f52c9d69b996" />
<img width="1373" height="673" alt="5" src="https://github.com/user-attachments/assets/9e5d7dfa-db5b-4aae-85d6-e80cd83af559" />
<img width="1386" height="536" alt="6" src="https://github.com/user-attachments/assets/50d8bf4c-b3b3-4a6c-a8c9-fd4f9f41d3b5" />
<img width="1391" height="426" alt="7" src="https://github.com/user-attachments/assets/83efd74a-9ae0-43a9-88cb-8d16a62e62da" />
<img width="1390" height="873" alt="8" src="https://github.com/user-attachments/assets/82e5c8ed-561a-445e-bf2d-3040020ca71d" />
<img width="1383" height="647" alt="9" src="https://github.com/user-attachments/assets/c8ae131c-d43b-42e3-b90a-d60ef51bdb4e" />

