# EXPENSE ENDPOINT

## ../api/v1/categories
- method: GET
- description: get all categories
- url: https://manhkhuat83.pythonanywhere.com/api/v1/categories
- additional params: page & size
- example url with pagination: https://manhkhuat83.pythonanywhere.com/api/v1/categories?page=1&size=2
- result:
    ```
    {
        "data": [
            {
                "id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
                "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
                "name": "Lương"
            },
            {
                "id": "f7bb37e7-3da7-488b-a6db-51802f452984",
                "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
                "name": "Ăn uống"
            }
        ],
        "page": 1,
        "size": 2
    }
    ```

- method: POST
- description: create new categories
- url: https://manhkhuat83.pythonanywhere.com/api/v1/categories
- required fields: name
- payload example:
    ```
    {
        "name": "Ăn uống"
    }
    ```
- result:
    ```
    {
        "id": "39bded12-01d7-4b2b-8bd5-534512d4e9ba",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "name": "Ăn uống"
    }
    ```


## ../api/v1/categories/{category_id}
- method: GET
- description: get category by category_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/categories/{category_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/categories/29b60e27-d87f-46dd-8cac-27d722a97ad3
- result:
    ```
    {
        "id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "name": "Lương"
    }
    ```

- method: PUT
- description: update category data by category_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/categories/{category_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/categories/29b60e27-d87f-46dd-8cac-27d722a97ad3
- changeable fields: name
- payload example:
    ```
    {
        "name": "Lương tháng"
    }
    ```
- result:
    ```
    {
        "id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "name": "Lương tháng"
    }
    ```

- method: DELETE
- description: delete category by category_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/categories/{category_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/categories/18e356e1-0af4-4c0c-a4bd-d2810f538e07
- result:
    ```
    {
        "msg": "Category deleted successfully"
    }
    ```


## .../api/v1/incomes
- method: GET
- description: get all incomes
- url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes
- additional params: page & size (int)
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes?page=1&size=2
- result:
    ```
    {
        "data": [
            {
            "id": "7e10d94b-0984-4f66-9d6b-3d9f7f73f04f",
            "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
            "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
            "description": "Lương tháng 11",
            "amount": 1000000.0,
            "date": "2022-11-09"
            },
            {
            "id": "d7db93e7-0c80-47c6-91ea-4debdb62e263",
            "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
            "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
            "description": "Lương tháng 10",
            "amount": 100000.0,
            "date": "2022-10-31"
            }
        ],
        "page": 1,
        "size": 2
    }
    ```

- method: POST
- description: create new income
- url:  https://manhkhuat83.pythonanywhere.com/api/v1/incomes
- required fields: category_id, description, amount, date (YYYY-mm-dd)
- payload example:
    ```
    {
        "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
        "description": "Lương tháng 10",
        "amount": 100000,
        "date": "2022-10-31"
    }
    ```
- result:
    ```
    {
        "id": "d7db93e7-0c80-47c6-91ea-4debdb62e263",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
        "description": "Lương tháng 10",
        "amount": 100000.0,
        "date": "2022-10-31"
    }
    ```


## .../api/v1/incomes/{income_id}
- method: GET
- description: get income by income_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes/{income_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes/7e10d94b-0984-4f66-9d6b-3d9f7f73f04f
- result:
    ```
    {
        "id": "7e10d94b-0984-4f66-9d6b-3d9f7f73f04f",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
        "description": "Lương tháng 11",
        "amount": 1000000.0,
        "date": "2022-11-09"
    }
    ```

- method: PUT
- description: update income by income_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/income/{income_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes/7e10d94b-0984-4f66-9d6b-3d9f7f73f04f
- changeable fields: category_id, description, amount, date
- payload example:
    ```
    {
        "amount": 100000,
        "date": "2022-11-30"
    }
    ```
- result:
    ```
    {
        "id": "7e10d94b-0984-4f66-9d6b-3d9f7f73f04f",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
        "description": "Lương tháng 11",
        "amount": 100000.0,
        "date": "2022-11-30"
    }
    ```

- method: DELETE
- description: delete income by income_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/income/{income_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes/7e10d94b-0984-4f66-9d6b-3d9f7f73f04f
- result:
    ```
    {
        "msg": "Income deleted successfully"
    }
    ```


## .../api/v1/expenses
- method: GET
- description: get all expenses
- url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses
- additional params: page & size (int)
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses?page=1&size=2
- result: 
    ```
    {
        "data": [
            {
                "id": "fd152d2b-7054-4685-b864-f8d7ff3f4309",
                "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
                "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
                "description": "Tiền ăn tháng 10",
                "amount": 500000.0,
                "date": "2022-10-31"
            },
            {
                "id": "63163cf0-8f77-4d64-b614-56727a33f4e9",
                "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
                "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
                "description": "Đi ăn ngoài",
                "amount": 30000.0,
                "date": "2022-10-31"
            }
        ],
        "page": 1,
        "size": 2
    }
    ```

- method: POST
- description: create new expenses
- url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses
- required fields: category_id, description, amount, date (YYYY-mm-dd)
- payload example:
    ```
    {
        "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
        "description": "Tiền ăn tháng 10",
        "amount": 500000,
        "date": "2022-10-31"
    }
    ```
- result:
    ```
    {
        "id": "fd152d2b-7054-4685-b864-f8d7ff3f4309",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
        "description": "Tiền ăn tháng 10",
        "amount": 500000.0,
        "date": "2022-10-31"
    }
    ```


## ../api/v1/expenses/{expense_id}
- method: GET
- description: get expense by expense_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses/{expense_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses/270f33e3-a042-42ff-bcca-7e7a204a0240
- result:
    ```
    {
        "id": "270f33e3-a042-42ff-bcca-7e7a204a0240",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
        "description": "Mua rau",
        "amount": 10000.0,
        "date": "2022-10-31"
    }
    ```

- method: PUT
- description: update expense by expense_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses/{expense_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses/270f33e3-a042-42ff-bcca-7e7a204a0240
- changeable fields: category_id, amount, description, date
- payload example:
    ```
    {
        "amount": 7000,
        "description": "Mua bim bim"
    }
    ```
- result:
    ```
    {
        "id": "270f33e3-a042-42ff-bcca-7e7a204a0240",
        "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
        "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
        "description": "Mua bim bim",
        "amount": 7000.0,
        "date": "2022-10-31"
    }
    ```

- method: DELETE
- description: delete expense by expense_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses/{expense_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/expenses/270f33e3-a042-42ff-bcca-7e7a204a0240
- result:
    ```
    {
        "msg": "Expense deleted successfully"
    }
    ```


## .../api/v1/incomes-expenses
- method: GET
- description: get all incomes, expense in a date
- url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes-expenses
- required params: date (YYYY-mm-dd)
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes-expenses?date=2022-10-31
- result:
    ```
    {
        "incomes": [
            {
            "id": "d7db93e7-0c80-47c6-91ea-4debdb62e263",
            "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
            "category_id": "29b60e27-d87f-46dd-8cac-27d722a97ad3",
            "description": "Lương tháng 10",
            "amount": 100000.0,
            "date": "2022-10-31"
            }
        ],
        "expenses": [
            {
            "id": "fd152d2b-7054-4685-b864-f8d7ff3f4309",
            "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
            "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
            "description": "Tiền ăn tháng 10",
            "amount": 500000.0,
            "date": "2022-10-31"
            },
            {
            "id": "63163cf0-8f77-4d64-b614-56727a33f4e9",
            "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
            "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
            "description": "Đi ăn ngoài",
            "amount": 30000.0,
            "date": "2022-10-31"
            }
        ],
        "total_incomes": 100000.0,
        "total_expenses": 530000.0,
        "date": "2022-10-31"
    }
    ```


## .../api/v1/incomes-expenses/category/{category_id}
- method: GET
- description: get all incomes, expenses by category_id
- url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes-expenses/category/{category_id}
- example url: https://manhkhuat83.pythonanywhere.com/api/v1/incomes-expenses/category/f7bb37e7-3da7-488b-a6db-51802f452984
- result:
    ```
    {
        "category": {
            "id": "f7bb37e7-3da7-488b-a6db-51802f452984",
            "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
            "name": "Ăn uống"
        },
        "incomes": [],
        "expenses": [
            {
                "id": "fd152d2b-7054-4685-b864-f8d7ff3f4309",
                "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
                "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
                "description": "Tiền ăn tháng 10",
                "amount": 500000.0,
                "date": "2022-10-31"
            },
            {
                "id": "63163cf0-8f77-4d64-b614-56727a33f4e9",
                "user_id": "dc29b535-98af-4b4a-85a2-d534a690c17d",
                "category_id": "f7bb37e7-3da7-488b-a6db-51802f452984",
                "description": "Đi ăn ngoài",
                "amount": 30000.0,
                "date": "2022-10-31"
            }
        ]
    }
    ```
