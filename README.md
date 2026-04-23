# Requirements:

Build a simple RESTful API using Django that performs CRUD operations on a database of bank accounts.
Implement error handling, use decorators, and demonstrate concurrency with async functions.

Setup Django Project:
Create a new Django project and app.
Set up a SQLite database.
Model:
Define a BankAccount model with fields: account_number, account_holder, balance.
API Endpoints:
Implement CRUD operations:
Create: POST /api/accounts/
Read: GET /api/accounts/<account_number>/
Update: PUT /api/accounts/<account_number>/
Delete: DELETE /api/accounts/<account_number>/
Error Handling:
Implement error handling for cases like account not found, invalid data, etc.
Decorators:
Write a decorator to log each API request and response.
Async Function:
Implement an async function to simulate fetching account details from an external service.


# Implementation

- The task is implemented using Django Rest Framework, and its asyncronous cousin `adrf`

- All `/api/accounts` endpoints are handled by a single drf viewset.

- The database backend is `mysql` from a generic Docker container. To spin it up, run (from the root of the repository):

`docker compose up --build -d`


- Only an `asgi` server is implemented to support the async features. To run (from `server` folder):

`uv run uvicorn server.asgi:application --reload --port 7000`


- The logging decorator uses the same function to return either a coroutine or a regular function based on the target's type.
An alternative implementation would be to split sync and async decorators completely.
