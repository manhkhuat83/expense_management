# DATABASE DESIGN

## User - Người dùng

| Column Name | Type          | Description       | Primary key   | Foreign key   |
|-------------|---------------|-------------------|---------------|---------------|
| id          | UUID          | Id người dùng     | x             |               |
| email       | String        | Email             |               |               |
| password    | Hashed string | Mật khẩu          |               |               |
| is_active   | Boolean       | Kích hoạt         |               |               |
| date_joined | Timestamp     | Ngày tạo          |               |               |


## Category - Danh mục thu chi

| Column Name | Type          | Description       | Primary key   | Foreign key   |
|-------------|---------------|-------------------|---------------|---------------|
| id          | UUID          | Id danh mục       | x             |               |
| user_id     | UUID          | Id người dùng     |               | x             |
| name        | String        | Tên danh mục      |               |               |


## Income - Khoản thu

| Column Name | Type          | Description       | Primary key   | Foreign key   |
|-------------|---------------|-------------------|---------------|---------------|
| id          | UUID          | Id khoản thu      | x             |               |
| user_id     | UUID          | Id người dùng     |               | x             |
| category_id | UUID          | Id danh mục       |               | x             |
| description | String        | Mô tả             |               |               |
| amount      | Float         | Số tiền           |               |               |
| date        | Timestamp     | Ngày chi          |               |               |


## Expense - Khoản chi

| Column Name | Type          | Description       | Primary key   | Foreign key   |
|-------------|---------------|-------------------|---------------|---------------|
| id          | UUID          | Id khoản chi      | x             |               |
| user_id     | UUID          | Id người dùng     |               | x             |
| category_id | UUID          | Id danh mục       |               | x             |
| description | String        | Mô tả             |               |               |
| amount      | Float         | Số tiền           |               |               |
| date        | Timestamp     | Ngày thu          |               |               |

