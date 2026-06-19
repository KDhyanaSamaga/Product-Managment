# Shopkeeper API Documentation

This documentation outlines the authentication and profile management endpoints for the Shopkeeper (User) module.

## 🔒 Security & Authentication

All protected endpoints require a valid bearer token. This can be provided in two ways:
1. **Authorization Header**: `Authorization: Bearer <your_token>`
2. **Cookies**: `access_token=Bearer <your_token>` (Automatically set upon login/signup)

Access will be denied (401 Unauthorized) if the token is missing, expired, or invalid.

---

## 🚀 Endpoints Summary

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| POST | `/user/signup` | No | Registers a new shopkeeper account with mandatory shop details. |
| POST | `/user/login` | No | Authenticates an existing shopkeeper and returns an access token. |
| POST | `/user/logout` | No | Logs out the current user by clearing the access token cookie. |
| GET | `/user/profile` | Yes | Retrieves the profile details of the logged-in shopkeeper. |
| PATCH | `/user/profile` | Yes | Updates specific profile or shop details. |
| PATCH | `/user/reset-password` | Yes | Changes the password while logged in using the old password. |

---

## 📑 Detailed Endpoint Specifications

### 1. SignUp
- **Method**: POST
- **Endpoint**: `/user/signup`
- **Description**: Creates a new shopkeeper account. All fields except `city` are mandatory.

**Request Body (JSON)**
```json
{
  "name": "John Doe",
  "phone_number": "9876543210",
  "email": "johndoe@example.com",
  "password": "SecurePassword123",
  "shop_name": "Doe Electronics",
  "shop_contact": "0824222333",
  "address": "123 Main Street, Industrial Area",
  "city": "Mangaluru",
  "gst": "29ABCDE1234F1Z5"
}
```

**Responses**
- **200 OK**: Account created successfully.
  ```json
  {
    "message": "Signup successful",
    "access_token": "eyJhbG...",
    "user_id": "uuid-here"
  }
  ```
- **400 Bad Request**: Missing mandatory fields, invalid format, or Email already registered.

### 2. Login
- **Method**: POST
- **Endpoint**: `/user/login`
- **Description**: Authenticates the shopkeeper. If credentials match, an access token is issued and set as an HTTP-only cookie.

**Request Body (JSON)**
```json
{
  "email": "johndoe@example.com",
  "password": "SecurePassword123"
}
```

**Responses**
- **200 OK**: Returns the authentication token.
  ```json
  {
    "message": "Login successful",
    "access_token": "eyJhbG..."
  }
  ```
- **401 Unauthorized**: Incorrect Password.
- **404 Not Found**: Email not found.

### 3. Logout
- **Method**: POST
- **Endpoint**: `/user/logout`
- **Description**: Logs out the shopkeeper by deleting the access token cookie.

**Responses**
- **200 OK**:
  ```json
  {
    "message": "Logout successful"
  }
  ```

### 4. Get Profile
- **Method**: GET
- **Endpoint**: `/user/profile`
- **Headers**: `Authorization: Bearer <token>`
- **Description**: Fetches the profile data of the currently authenticated shopkeeper.

**Responses**
- **200 OK**: Returns complete shopkeeper and shop details.
  ```json
  {
    "name": "John Doe",
    "phone_number": "9876543210",
    "shop_name": "Doe Electronics",
    "shop_contact": "0824222333",
    "email": "johndoe@example.com",
    "address": "123 Main Street, Industrial Area",
    "city": "Mangaluru",
    "gst": "29ABCDE1234F1Z5"
  }
  ```
- **401 Unauthorized**: Invalid or missing token.

### 5. Update Profile
- **Method**: PATCH
- **Endpoint**: `/user/profile`
- **Headers**: `Authorization: Bearer <token>`
- **Description**: Modifies partial details of the profile or shop. All fields are optional.

**Request Body (JSON - Optional Fields)**
```json
{
  "shop_name": "Doe Digital & Electronics",
  "shop_contact": "0824222444"
}
```

**Responses**
- **200 OK**: Profile updated successfully. Returns the updated profile.
- **401 Unauthorized**: Invalid or missing token.

### 6. Reset Password (Change Password)
- **Method**: PATCH
- **Endpoint**: `/user/reset-password`
- **Headers**: `Authorization: Bearer <token>`
- **Description**: Updates the account password using the current active password.

**Request Body (JSON)**
```json
{
  "old_password": "SecurePassword123",
  "new_password": "NewSuperSecure456",
  "confirm_password": "NewSuperSecure456"
}
```

**Responses**
- **200 OK**: Password changed successfully.
  ```json
  {
    "message": "Password updated successfully"
  }
  ```
- **400 Bad Request**: Passwords do not match.
- **401 Unauthorized**: Authentication failed or Incorrect old password.
