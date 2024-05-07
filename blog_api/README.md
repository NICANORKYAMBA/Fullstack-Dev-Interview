## Blog Post API Documentation

This document provides a comprehensive guide to the Blog Post REST API. It outlines the functionalities, endpoints, authentication, request formats, response structures, and error handling for interacting with blog posts.

### 1. Introduction

This API allows you to manage blog posts, including creating, retrieving, updating, and deleting them. Authentication is required for most operations, except retrieving a list of posts.

### 2. Endpoints

Here's a table summarizing the available API endpoints

| Endpoint                     | HTTP Method | Description                                                    | Authentication Required |
|------------------------------|-------------|-----------------------------------------------------------------|-------------------------|
| `/api/posts/`                 | GET          | Retrieves a list of all blog posts.                            | No                       |
| `/api/posts/<int:pk>/`       | GET          | Retrieves a specific blog post by its ID.                     | No                       |
| `/api/posts/`                 | POST         | Creates a new blog post.                                         | Yes                      |
| `/api/posts/<int:pk>/`       | PUT          | Updates an existing blog post.                                   | Yes                      |
| `/api/posts/<int:pk>/`       | DELETE       | Deletes an existing blog post.                                   | Yes                      |
| `/api/register/`             | POST         | Registers a new user (optional, for authentication).           | No                       |
| `/api/token/`                | POST         | Obtains an authentication token for subsequent requests.         | No                       |
| `/api/token/refresh/`         | POST         | Refreshes an expired authentication token.                       | Yes                      |


**Note**

- `<int:pk>` represents the primary key (ID) of a specific blog post.

### 3. Authentication

The API uses token-based authentication (JSON Web Tokens - JWT). To perform actions that modify blog posts (create, update, delete), you need to obtain an authentication token and include it in the Authorization header of your requests.

**3.1 Obtaining a Token**

Use the `/api/token/` endpoint with a POST request to generate a JWT token. You'll need to provide valid user credentials (username and password) in the request body.

**Request Body**

```json
{
  "username": "username",
  "password": "password"
}
```

**Response**

Upon successful login, the response will contain a JSON object with the following fields

```json
{
  "access": "access_token",
  "refresh": "refresh_token"
}
```

- `access`: The access token used for subsequent authorized requests. Include it in the Authorization header with the `Bearer` scheme (e.g., `Authorization: Bearer access_token`). This token has a limited lifespan.
- `refresh`: The refresh token used to obtain a new access token when the current one expires.

**3.2 Refreshing an Expired Token**

Use the `/api/token/refresh/` endpoint with a POST request to refresh an expired access token. Include the refresh token obtained during login in the request body.

**Request Body**

```json
{
  "refresh": "refresh_token"
}
```

**Response**

Upon successful refresh, the response will contain a new access token

```json
{
  "access": "new_access_token"
}
```

### 4. Request Formats

The API accepts requests in JSON format. Here's an example of a JSON request body for creating a new blog post

```json
{
  "title": "My New Blog Post",
  "content": "This is the content of my blog post."
}
```

### 5. Response Structures

The API responses are also in JSON format. The structure of the response depends on the endpoint and operation performed. Here is an example

**Retrieving a list of blog posts**

```json
[
  {
    "id": 1,
    "author": "john.doe",
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post.",
    "created_at": "2024-05-06T18:26:39.789203Z",
    "updated_at": "2024-05-06T18:26:39.789262Z"
  },
]
```

**Error Handling**

The API uses standard HTTP status codes to indicate success or failure. Here are some examples

- **200 OK:** Successful request.
- **201 Created:** Resource created successfully (e.g., creating a new blog post).
- **400 Bad Request:** Invalid request format or missing required data.
- **401 Unauthorized:** Missing or invalid authentication token.
- **403 Forbidden:** Insufficient permissions to perform the requested action.
- **404 Not Found:** The requested resource (e.g., a blog post with a specific ID) could not be found.
- **500 Internal Server Error:** An unexpected error occurred on the server side.

The error response body might include additional details about the specific error encountered.

### 6. Running the Server

To run the server and start using the Blog Post API, follow these steps:

1. **Install Dependencies**
Make sure you have all the required dependencies installed. You can install them using pip.

   ```bash
   pip install -r requirements.txt
   ```

2. **Migrate Database**
If you're using a database, run the migrations to apply any pending changes.

   ```bash
   python manage.py migrate
   ```

3. **Start the Server**
Run the Django development server.

   ```bash
   python manage.py runserver
   ```

4. **Access the API**
nce the server is running, you can access the API endpoints using your preferred HTTP client (e.g., cURL, Postman). Here are some example requests:

   - **Get All Blog Posts**:
     ```bash
     curl -X GET http://localhost:8000/api/posts/
     ```

   - **Get a Single Blog Post** (replace `<post_id>` with the actual ID of the post):
     ```bash
     curl -X GET http://localhost:8000/api/posts/<post_id>/
     ```

   - **Create a New Blog Post**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"title":"New Post","content":"This is the content of my new post."}' http://localhost:8000/api/posts/
     ```

   - **Update an Existing Blog Post** (replace `<post_id>` with the actual ID of the post):
     ```bash
     curl -X PUT -H "Content-Type: application/json" -d '{"title":"Updated Post","content":"This is the updated content of my post."}' http://localhost:8000/api/posts/<post_id>/
     ```

   - **Delete a Blog Post** (replace `<post_id>` with the actual ID of the post):
     ```bash
     curl -X DELETE http://localhost:8000/api/posts/<post_id>/
     ```

5. **Authentication**
For endpoints that require authentication (e.g., creating, updating, deleting posts), obtain an authentication token by sending a POST request to `/api/token/` with valid user credentials. Use the obtained token in the `Authorization` header for subsequent requests.

6. **Explore Other Endpoints**
Feel free to explore other endpoints provided by the API, such as user registration (`/api/register/`) and token refresh (`/api/token/refresh/`).
