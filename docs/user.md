# User Endpoint


## .../api/v1/user/register
- method: POST
- description: register new user
- payload:
    ```
    {
        "email": "admin@gmail.com",
        "password": "admin"
    }
    ```
- response:
    ```
    {
        "id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "email": "admin@gmail.com",
        "is_active": true,
        "date_joined": "2022-12-19"
    }
    ``` 


## .../api/v1/token/auth
- method: POST
- description: login for access token
- payload:
    ```
    {
        "email": "admin@gmail.com",
        "password": "admin"
    }
    ```
- response:
    ```
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDA0OTI3NCwiaWF0IjoxNjcxNDU3Mjc0LCJqdGkiOiJjMWRjZmMyZGZhZjg0ZTc0YTM2Yjg3NDliYWZiMWQ5OCIsInVzZXJfaWQiOiI5MzdkMmRmZS0xNjY4LTQ5MDctODY0My1hNDE5ZTYxN2FjMTgifQ.Md7d6vf6RdD6st0evyk5OzPeQGl3YNlM4L5fJwx15z8",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNTQzNjc0LCJpYXQiOjE2NzE0NTcyNzQsImp0aSI6IjUyM2Q1MzQwNDg1YTQ0MDI5NzhjMzU3ODYyNmU1ZjkxIiwidXNlcl9pZCI6IjkzN2QyZGZlLTE2NjgtNDkwNy04NjQzLWE0MTllNjE3YWMxOCJ9.WJT5BUb_0weKAjTFvx95jQR8_IvThP9VU0cuyj2LqSw"
    }
    ```


## .../api/v1/user/self
- method: GET
- description: get self information
- response:
    ```
    {
        "id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "email": "admin@gmail.com",
        "is_active": true,
        "date_joined": "2022-12-19"
    }
    ```

- method: PUT
- description: change password
- payload:
    ```
    {
        "current_password": "admin",
        "new_password": "test"
    }
    ```
- response:
    ```
    {
        "msg": "Changed"
    }
    ```