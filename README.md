# Installation

To run this FastAPI Todo API project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/everest1508/todo-list-fast-api.git
s

# FastAPI Todo API Reference

This API reference provides details on the endpoints, methods, and parameters for a FastAPI project that allows user authentication, registration, and managing todo tasks.

## Authentication

### Login

POST /api/auth/login

Authenticate users and receive an access token.

#### Request

```
{
"email": "string",
"password": "string"
}
```

#### Response

- **200 OK**: Successful authentication. Returns access token.
- **401 Unauthorized**: Invalid credentials.

### Register

POST /api/auth/register

Register new users.

#### Request

```
{
"username": "string",
"email": "string",
"password": "string"
}
```

#### Response

- **201 Created**: User successfully registered.
- **400 Bad Request**: Invalid username or password.

## Todo

### List Todo

GET /api/todo/

Retrieve a list of todo tasks.

#### Request

No parameters required.

#### Response

```
[
    {
        "id": integer,
        "task": "string",
        "done": boolean
    }
]
```

### Create Todo

POST /api/todo/

```
{
    "task": "string",
    "done": boolean
}
```

#### Response

- **201 Created**: Todo task created successfully.
- **400 Bad Request**: Invalid task data.

### Update Todo

PUT /api/todo/{key}

#### Request

```
{
    "task": "string",
    "done": boolean
}
```

#### Response

- **200 OK**: Todo task updated successfully.
- **404 Not Found**: Todo task not found.

### Delete Todo

DELETE api/todo/{key}

#### Request

No body needed

#### Response

- **200 OK**: Todo task deleted successfully.
- **404 Not Found**: Todo task not found.

## Database Configuration

The API supports both MySQL and SQLite databases. You can configure the database in the `.env` file.

* To use MySQL, set 
 DB_URL = `mysql://{username}:{password}@localhost:{port_no}/{database_name}`
 in the `.env` file and provide the necessary MySQL connection details. In my case the user name is **root**, password is **None** port number is  **3306** and the database name is  **todo-list** 
```
eg : mysql://root:@localhost:3306/todo-list
```
* To use SQLite, set `DB_URL = sqlite://todo-list.sqlite3` in the `.env` file.
