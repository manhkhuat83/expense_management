# Statistic Endpoint


## .../api/v1/statistic/common
- method: GET
- description: get total income/expense per date in range time
- required parameter: start_date, end_date (YYYY-mm-dd)
- url: .../api/v1/statistic/common?start_date=2022-11-30&end_date=2022-12-20
- response:
    ```
    {
    "data": [
        {
        "date": "2022-11-30",
        "total_incomes": 1500000,
        "total_expenses": 0
        },
        {
        "date": "2022-12-01",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-02",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-03",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-04",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-05",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-06",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-07",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-08",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-09",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-10",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-11",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-12",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-13",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-14",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-15",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-16",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-17",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-18",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-19",
        "total_incomes": 0,
        "total_expenses": 0
        },
        {
        "date": "2022-12-20",
        "total_incomes": 0,
        "total_expenses": 550000
        }
    ]
    }
    ```


## .../api/v1/statistic/income
- method: GET
- description: get statistic income per date in range time
- required parameter: start_date, end_date (YYYY-mm-dd)
- url: .../api/v1/statistic/income?start_date=2022-11-30&end_date=2022-12-20
- response:
    ```
    {
        "Salary": 1000000,
        "Bonus": 500000,
        "total_incomes": 1500000
    }
    ```


## .../api/v1/statistic/expense
- method: GET
- description: get statistic expense per date in range time
- required parameter: start_date, end_date (YYYY-mm-dd)
- url: .../api/v1/statistic/expense?start_date=2022-11-30&end_date=2022-12-20
- response:
    ```
    {
        "Fashion": 250000,
        "Shopping": 300000,
        "total_expenses": 550000
    }
    ```