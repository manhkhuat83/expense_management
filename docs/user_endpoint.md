# USER ENDPOINT


## .../api/v1/user/register
- method: POST
- description: register user account
- url: https://manhkhuat83.pythonanywhere.com/api/v1/user/register
- required fields: email, password
- payload:
    ```
    {
        "email": "admin@gmail.com",
        "password": "admin"
    }
    ```
- result:
    ```
    {
        "id": "bc293d33-813b-4829-8d6a-1fe705a62997",
        "email": "admin@gmail.com",
        "is_active": true,
        "date_joined": "2022-11-09"
    }
    ```


## .../api/v1/token/auth
- method: POST
- description: get access token for login
- url: https://manhkhuat83.pythonanywhere.com/api/v1/token/auth
- required fields: email, password
- payload:
    ```
    {
        "email": "admin@gmail.com",
        "password": "admin"
    }
    ```
- result:
    ```
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDU3NTEyMSwiaWF0IjoxNjY3OTgzMTIxLCJqdGkiOiI3N2IzMTRhOGRiNTI0OTI1YmE3YjQyOWM2MzlhYjBmNiIsInVzZXJfaWQiOiI0N2FiNzc5Ny05MTlkLTQxYTktODhlNC04YmEzOWI3MmM0NTEifQ._jnM4LnNPsOVBrMoVoFjJQbJpawbhETJgSbQ6wIWrxQ",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MDY5NTIxLCJpYXQiOjE2Njc5ODMxMjEsImp0aSI6ImExMmYxMzQ2YWY5MjRhYzM4ZTMwYWNiNDY4OGM4Y2ZjIiwidXNlcl9pZCI6IjQ3YWI3Nzk3LTkxOWQtNDFhOS04OGU0LThiYTM5YjcyYzQ1MSJ9.ivhKrTP3EuKJjkgy4rFGDC_KfJcLLCW7JyENMdvSOZs"
    }
    ```


## .../api/v1/token/refresh
- method: POST
- description: get new access token from refresh token
- url: https://manhkhuat83.pythonanywhere.com/api/v1/token/refresh
- required fields: refresh
- payload:
    ```
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjIzNDQ5MiwiaWF0IjoxNjYzNjQyNDkyLCJqdGkiOiJmMzQ1NGYwZWRhYjE0Y2RlYTM1OGUyNTI0MmUwMzMyMyIsInVzZXJfaWQiOiIyMzJhODM5Yy04ZGNiLTRlYzgtOGJkMi05ZmFmOGUxODA1NWIifQ.O5m7x0A08_simLU8ZMv97ZUDhKPTJTPrGe4NnOlv5fg"
    }
    ```
- result:
    ```
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NjIzNDQ5MiwiaWF0IjoxNjYzNjQyNDkyLCJqdGkiOiJmMzQ1NGYwZWRhYjE0Y2RlYTM1OGUyNTI0MmUwMzMyMyIsInVzZXJfaWQiOiIyMzJhODM5Yy04ZGNiLTRlYzgtOGJkMi05ZmFmOGUxODA1NWIifQ.O5m7x0A08_simLU8ZMv97ZUDhKPTJTPrGe4NnOlv5fg",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNzI4ODkyLCJpYXQiOjE2NjM2NDI0OTIsImp0aSI6Ijg5NjI3ZmZiZjU0OTQ3MmY4NDU5Y2U0YThjMTYyNWEzIiwidXNlcl9pZCI6IjIzMmE4MzljLThkY2ItNGVjOC04YmQyLTlmYWY4ZTE4MDU1YiJ9.uuZ5hfnAIWasAQpbHZ2xFIUdwpXupukJlfRTDnHgBTw"
    }
    ```


## .../api/v1/user/self
- method: GET
- description: get self information
- url: https://manhkhuat83.pythonanywhere.com/api/v1/user/self
- result:
    ```
    {
        "id": "47ab7797-919d-41a9-88e4-8ba39b72c451",
        "email": "admin@gmail.com",
        "is_active": true,
        "date_joined": "2022-11-09"
    }
    ```


- method: PUT
- description: change self password
- url: https://manhkhuat83.pythonanywhere.com/api/v1/user/self
- required fields: current_password, new_password
- payload:
    ```
    {
        "current_password": "admin",
        "new_password": "admin123"
    }
    ```
- result:
    ```
    {
        "msg": "Password changed successfully"
    }
    ```