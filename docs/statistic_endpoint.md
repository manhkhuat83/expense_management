# STATISTIC ENDPOINT


## .../api/v1/statistic
- method: GET
- description: get statistic of income/expense during a time
- url: https://manhkhuat83.pythonanywhere.com/api/v1/statistic
- required params: start_date, end_date (YYYY-mm-dd)
- url example: https://manhkhuat83.pythonanywhere.com/api/v1/statistic?start_date=2022-10-29&end_date=2022-11-03
- result:
    ```
    {
        "data": [
            {
                "date": "2022-10-29",
                "total_incomes": 0,
                "total_expenses": 0
            },
            {
                "date": "2022-10-30",
                "total_incomes": 0,
                "total_expenses": 0
            },
            {
                "date": "2022-10-31",
                "total_incomes": 100000.0,
                "total_expenses": 530000.0
            },
            {
                "date": "2022-11-01",
                "total_incomes": 0,
                "total_expenses": 0
            },
            {
                "date": "2022-11-02",
                "total_incomes": 0,
                "total_expenses": 0
            },
            {
                "date": "2022-11-03",
                "total_incomes": 0,
                "total_expenses": 0
            }
        ]
    }
    ```