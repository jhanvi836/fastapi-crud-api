# Product Management RESTful API

A robust RESTful API built with **FastAPI**, **SQLAlchemy ORM**, and **Pydantic** for managing a product inventory. Includes complete CRUD operations, input validation, automatic database migrations (table creation), and interactive OpenAPI documentation.

## Features

- **Fast API Framework**: Fast execution and automatic interactive docs.
- **Data Validation**: Strict type checking and validation via Pydantic schemas.
- **Database Integration**: SQLAlchemy supporting SQLite (default) and PostgreSQL.
- **Standardized Errors**: Proper HTTP status codes and JSON error structures.

---

## Data Models

### Product Schema

| Field         | Type     | Required | Description                               |
|---------------|----------|----------|-------------------------------------------|
| `id`          | Integer  | Auto     | Unique primary key identifier             |
| `name`        | String   | Yes      | Name of product (1-100 characters)        |
| `description` | String   | No       | Product description (max 255 chars)       |
| `price`       | Float    | Yes      | Product price (must be > 0)               |
| `in_stock`    | Boolean  | Optional | Stock status (default: `true`)            |
| `created_at`  | DateTime | Auto     | Timestamp of creation                     |
| `updated_at`  | DateTime | Auto     | Timestamp of last update                  |

---

## API Endpoints Summary

| Method   | Endpoint                  | Status Code | Description                   |
|----------|---------------------------|-------------|-------------------------------|
| `POST`   | `/api/v1/products`        | `201`       | Create a new product          |
| `GET`    | `/api/v1/products`        | `200`       | Get all products (paginated)  |
| `GET`    | `/api/v1/products/{id}`   | `200`       | Get a product by ID           |
| `PUT`    | `/api/v1/products/{id}`   | `200`       | Update a product by ID        |
| `DELETE` | `/api/v1/products/{id}`   | `204`       | Delete a product by ID        |

---

## Local Setup & Installation

### Prerequisites
- Python 3.9+
- `pip` and `virtualenv`

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/your-username/fastapi-crud-api.git](https://github.com/your-username/fastapi-crud-api.git)
   cd fastapi-crud-api