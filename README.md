# FastAPI + MySQL Product Synchronization and Management Service

## Project Overview

This project is an enterprise-style backend service built using FastAPI and MySQL.

The application supports:

* Product synchronization from external APIs
* Product management APIs
* Favorites management APIs
* Pagination
* Searching
* Filtering
* Sorting
* Role-based authorization
* Stored procedure-based database operations

---

# Tech Stack

* FastAPI
* MySQL
* SQLAlchemy
* PyMySQL
* Pydantic
* Stored Procedures
* Python

---

# Project Architecture

The application follows layered enterprise architecture:

```text
API Route
→ Service Layer
→ Repository Layer
→ Stored Procedure Executor
→ MySQL Stored Procedures
```

---

# Project Structure

```text
app/
├── api/v1/
├── services/
├── repositories/
├── utils/
├── core/
├── schemas/
```

---

# Features Implemented

## Product APIs

* Product synchronization
* Get all products
* Get product by ID
* Search products
* Filter products
* Sorting
* Pagination
* Delete product

## Favorites APIs

* Add favorite
* Remove favorite
* Get favorites

## Security

* Role-based authorization
* User role validation using database
* X-User-Id header authentication

---

# API Endpoints

## Product APIs

### Sync Products

```http
POST /api/v1/sync/products
```

Admin only.

Synchronizes products from:

```text
https://fakestoreapi.com/products
```

---

### Get Products

```http
GET /api/v1/products
```

Supports:

* Pagination
* Sorting

Query Parameters:

| Parameter | Description      |
| --------- | ---------------- |
| page      | Page number      |
| limit     | Records per page |
| sort_by   | Sorting field    |
| order     | asc / desc       |

---

### Search Products

```http
GET /api/v1/products/search
```

Supports:

* Keyword search
* Pagination
* Sorting

---

### Filter Products

```http
GET /api/v1/products/filter
```

Supports:

* Category filtering
* Pagination
* Sorting

---

### Get Product By ID

```http
GET /api/v1/products/{product_id}
```

---

### Delete Product

```http
DELETE /api/v1/products/{product_id}
```

Admin only.

---

# Favorites APIs

### Add Favorite

```http
POST /api/v1/favorites/{product_id}
```

Subscriber only.

---

### Remove Favorite

```http
DELETE /api/v1/favorites/{product_id}
```

Subscriber only.

---

### Get Favorites

```http
GET /api/v1/favorites
```

Subscriber only.

---

# Authentication

Authentication uses request header:

```http
X-User-Id
```

User roles are retrieved from:

```text
wpgo_users
```

Supported roles:

* administrator
* subscriber

---

# Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=your_database
```

---

# How To Run The Application

## Step 1 — Clone Repository

```bash
git clone <repository_url>
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3 — Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Configure Environment Variables

Create `.env` file.

---

## Step 6 — Setup Database

Run:

* Table creation scripts
* Stored procedure scripts

---

## Step 7 — Run Application

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# How To Test APIs

## Using Swagger

1. Open Swagger UI
2. Expand endpoint
3. Click "Try it out"
4. Provide request parameters
5. Add:

```http
X-User-Id
```

header

6. Execute request

---

# Example Headers

## Admin User

```http
X-User-Id: 1
```

## Subscriber User

```http
X-User-Id: 2
```

---

# Database Scripts

The repository includes:

* Table creation scripts
* Stored procedure scripts
* Constraint definitions
* Foreign keys

---

# Important Database Tables

## tblFastAPIProducts

Stores synchronized product data.

## tblFastAPIFavorites

Stores user favorite mappings.

## wpgo_users

Stores user role information.

---

# Stored Procedures Used

Examples:

* usp_UpsertProduct
* usp_GetProducts
* usp_GetProductById
* usp_SearchProducts
* usp_FilterProducts
* usp_DeleteProduct
* usp_AddFavorite
* usp_RemoveFavorite
* usp_GetFavorites
* sp_GetUserRole

---

# API Features

* RESTful APIs
* Layered architecture
* Stored procedure integration
* Pagination
* Filtering
* Searching
* Sorting
* Role-based access control
* Pydantic validation
* Swagger support

---

# Future Improvements

* JWT Authentication
* Unit Testing
* Docker Support
* Logging
* Centralized Exception Handling
* Redis Caching
* CI/CD Integration

---

# Author

Ayush
