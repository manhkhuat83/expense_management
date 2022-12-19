# Expense Endpoint


## .../api/v1/income-categories
- method: GET
- description: get all income categories
- response:
    ```
    [
        {
            "id": "babdfc9c-81a1-4495-b684-24285d73d894",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "name": "Salary"
        },
        {
            "id": "e64025a1-b1ea-40cf-bdc8-e42db7c8afb5",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "name": "Bonus KPI"
        }
    ]
    ```


- method: POST
- description: create new income categories
- payload:
    ```
    {
        "name": "Salary"
    }
    ```
- response:
    ```
    {
        "id": "babdfc9c-81a1-4495-b684-24285d73d894",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "name": "Salary"
    }
    ```


## .../api/v1/income-categories/{income_category_id}
- method: GET
- description: get income category by id
- url: .../api/v1/income-categories/e64025a1-b1ea-40cf-bdc8-e42db7c8afb5
- response:
    ```
    {
        "id": "e64025a1-b1ea-40cf-bdc8-e42db7c8afb5",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "name": "Bonus KPI"
    }
    ```

- method: PUT
- description: update income category by id
- url: .../api/v1/income-categories/e64025a1-b1ea-40cf-bdc8-e42db7c8afb5
- payload:
    ```
    {
        "name": "Bonus"
    }
    ```
- response:
    ```
    {
        "id": "e64025a1-b1ea-40cf-bdc8-e42db7c8afb5",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "name": "Bonus"
    }
    ```

- method: DELETE
- description: delete income category by id
- url: .../api/v1/income-categories/e64025a1-b1ea-40cf-bdc8-e42db7c8afb5
- response:
    ```
    {
        "msg": "Deleted"
    }
    ```


## .../api/v1/expense-categories
- method: GET
- description: get all expense categories
- response:
    ```
    [
        {
            "id": "a57dace0-4a51-42a2-9d35-b5f3f3845fd8",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "name": "Fashion"
        },
        {
            "id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "name": "Electric bill"
        }
    ]
    ```

- method: POST
- description: create new expense categories
- payload:
    ```
    {
        "name": "Electric bill"
    }
    ```
- response:
    ```
    {
        "id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "name": "Electric bill"
    }
    ```


## .../api/v1/expense-categories/{expense_category_id}
- method: GET
- description: get expense category by id
- url: ...api/v1/expense-categories/b7932c22-8587-4c14-971f-bf68b2f7101a
- response:
    ```
    {
        "id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "name": "Electric bill"
    }
    ```

- method: PUT
- description: update expense category by id
- url: .../api/v1/expense-categories/b7932c22-8587-4c14-971f-bf68b2f7101a
- payload:
    ```
    {
        "name": "Shopping"
    }
    ```
- response:
    ```
    {
        "id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "name": "Shopping"
    }
    ```

- method: DELETE
- description: delete expense category by id
- url: ...api/v1/expense-categories/b7932c22-8587-4c14-971f-bf68b2f7101a
- response:
    ```
    {
        "msg": "Deleted"
    }
    ```

## .../api/v1/incomes
- method: GET
- description: get all incomes
- response:
    ```
    [
        {
            "id": "32762305-9f87-4abf-af91-12ad97f7d951",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "income_category_id": "e64025a1-b1ea-40cf-bdc8-e42db7c8afb5",
            "description": "Bonus KPI month 12",
            "amount": 1000000,
            "date": "2022-12-30"
        },
        {
            "id": "b4ae15ba-4c07-45cc-b88a-4c733c0753d8",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "income_category_id": "babdfc9c-81a1-4495-b684-24285d73d894",
            "description": "Salary month 11",
            "amount": 1000000,
            "date": "2022-11-30"
        }
    ]
    ```

- method: POST
- description: create new income
- payload:
    ```
    {
        "income_category_id": "babdfc9c-81a1-4495-b684-24285d73d894",
        "description": "Salary month 11",
        "amount": 1000000,
        "date": "2022-11-30"
    }
    ```
- response:
    ```
    {
        "id": "b4ae15ba-4c07-45cc-b88a-4c733c0753d8",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "income_category_id": "babdfc9c-81a1-4495-b684-24285d73d894",
        "description": "Salary month 11",
        "amount": 1000000,
        "date": "2022-11-30"
    }
    ```


## .../api/v1/incomes/{income_id}
- method: GET
- description: get income by id
- url: .../api/v1/incomes/32762305-9f87-4abf-af91-12ad97f7d951
- response:
    ```
    {
        "id": "32762305-9f87-4abf-af91-12ad97f7d951",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "income_category_id": "e64025a1-b1ea-40cf-bdc8-e42db7c8afb5",
        "description": "Bonus KPI month 12",
        "amount": 1000000,
        "date": "2022-12-30"
    }
    ```

- method: PUT
- description: update income by id
- url: .../api/v1/incomes/32762305-9f87-4abf-af91-12ad97f7d951
- payload:
    ```
    {
        "description": "Bonus Tet holiday",
        "amount": 50000
    }
    ```
- response:
    ```
    {
        "id": "32762305-9f87-4abf-af91-12ad97f7d951",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "income_category_id": "e64025a1-b1ea-40cf-bdc8-e42db7c8afb5",
        "description": "Bonus Tet holiday",
        "amount": 50000,
        "date": "2022-12-30"
    }
    ```

- method: DELETE
- description: delete income by id
- url: .../api/v1/incomes/32762305-9f87-4abf-af91-12ad97f7d951
- response:
    ```
    {
        "msg": "Deleted"
    }
    ```


## .../api/v1/expenses
- method: GET
- description: get all expenses
- response:
    ```
    [
        {
            "id": "1a2f257b-1677-4e5b-8973-dd0c45eb1c0c",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
            "description": "Buy T-shirt",
            "amount": 150000,
            "date": "2022-12-20"
        },
        {
            "id": "51a2c38f-3f4a-46a1-85b9-c0e3da476846",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "a57dace0-4a51-42a2-9d35-b5f3f3845fd8",
            "description": "Buy Chelsea Boot",
            "amount": 150000,
            "date": "2022-12-20"
        }
    ]
    ```

- method: POST
- description: create new expense
- payload:
    ```
    {
        "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
        "description": "Buy T-shirt",
        "amount": 150000,
        "date": "2022-12-20"
    }
    ```
- response:
    ```
    {
        "id": "1a2f257b-1677-4e5b-8973-dd0c45eb1c0c",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
        "description": "Buy T-shirt",
        "amount": 150000,
        "date": "2022-12-20"
    }
    ```


## .../api/v1/expenses/{expense_id}
- method: GET
- description: get expense by id
- url: .../api/v1/expenses/51a2c38f-3f4a-46a1-85b9-c0e3da476846
- response:
    ```
    {
        "id": "51a2c38f-3f4a-46a1-85b9-c0e3da476846",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "expense_category_id": "a57dace0-4a51-42a2-9d35-b5f3f3845fd8",
        "description": "Buy Chelsea Boot",
        "amount": 150000,
        "date": "2022-12-20"
    }
    ```

- method: PUT
- description: update expense by id
- url: .../api/v1/expenses/51a2c38f-3f4a-46a1-85b9-c0e3da476846
- payload:
    ```
    {
        "description": "Buy Doctor Martens",
        "amount": 250000
    }
    ```
- response:
    ```
    {
        "id": "51a2c38f-3f4a-46a1-85b9-c0e3da476846",
        "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
        "expense_category_id": "a57dace0-4a51-42a2-9d35-b5f3f3845fd8",
        "description": "Buy Doctor Martens",
        "amount": 250000,
        "date": "2022-12-20"
    }
    ```

- method: DELETE
- description: delete expense by id
- url: .../api/v1/expenses/51a2c38f-3f4a-46a1-85b9-c0e3da476846
- response:
    ```
    {
        "msg": "Deleted"
    }
    ```


## .../api/v1/income-categories/{income_category_id}/incomes
- method: GET
- description: get all incomes of category by income category id
- url: .../api/v1/income-categories/babdfc9c-81a1-4495-b684-24285d73d894/incomes
- response:
    ```
    [
        {
            "id": "b4ae15ba-4c07-45cc-b88a-4c733c0753d8",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "income_category_id": "babdfc9c-81a1-4495-b684-24285d73d894",
            "description": "Salary month 11",
            "amount": 1000000,
            "date": "2022-11-30"
        },
        {
            "id": "bc8309f1-6adf-4dfa-8b94-fc37a6e96237",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "income_category_id": "babdfc9c-81a1-4495-b684-24285d73d894",
            "description": "Salary month 12",
            "amount": 1000000,
            "date": "2022-12-30"
        }
    ]
    ```


## .../api/v1/expense-categories/{expense_category_id}/expenses
- method: GET
- description: get all expense of category by expense category id
- url: .../api/v1/expense-categories/b7932c22-8587-4c14-971f-bf68b2f7101a/expenses
- response:
    ```
    [
        {
            "id": "1a2f257b-1677-4e5b-8973-dd0c45eb1c0c",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
            "description": "Buy T-shirt",
            "amount": 150000,
            "date": "2022-12-20"
        },
        {
            "id": "dc6de62d-c056-4a90-b281-6349ef1e06bd",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
            "description": "Buy Jacket",
            "amount": 150000,
            "date": "2022-12-20"
        }
    ]
    ```


## .../api/v1/income-expense
- method: GET
- description: get income and expense by date 
- required parameter: date (YYYY-mm-dd)
- url: .../api/v1/income-expense?date=2022-12-20
- response:
    ```
    {
        "incomes": [],
        "expenses": [
            {
            "id": "1a2f257b-1677-4e5b-8973-dd0c45eb1c0c",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
            "description": "Buy T-shirt",
            "amount": 150000,
            "date": "2022-12-20"
            },
            {
            "id": "51a2c38f-3f4a-46a1-85b9-c0e3da476846",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "a57dace0-4a51-42a2-9d35-b5f3f3845fd8",
            "description": "Buy Doctor Martens",
            "amount": 250000,
            "date": "2022-12-20"
            },
            {
            "id": "dc6de62d-c056-4a90-b281-6349ef1e06bd",
            "user_id": "937d2dfe-1668-4907-8643-a419e617ac18",
            "expense_category_id": "b7932c22-8587-4c14-971f-bf68b2f7101a",
            "description": "Buy Jacket",
            "amount": 150000,
            "date": "2022-12-20"
            }
        ],
        "total_incomes": 0,
        "total_expenses": 550000,
        "date": "2022-12-20"
    }
    ```