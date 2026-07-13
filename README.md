# Instagram Clone API

A REST API for an Instagram Clone built with Django and Django REST Framework.

## Features

- User registration
- JWT Authentication
- Email/Phone verification
- Custom User model
- User profile
- Create, update and delete posts
- Like and unlike posts
- Comment on posts
- Like and unlike comments
- Pagination
- PostgreSQL database

## Tech Stack

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- Pipenv
- JWT (Simple JWT)

## Project Structure

```
instagram_clone/
│
├── instagram_clone/
├── users/
├── post/
├── shared/
├── manage.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/khasanmukhammad/instagram_clone.git
```

Move to the project folder

```bash
cd instagram_clone
```

Install dependencies

```bash
pipenv install
```

Activate virtual environment

```bash
pipenv shell
```

Create a `.env` file

Example:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_password
```

Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```

Server:

```
http://127.0.0.1:8000/
```

## API Endpoints

### Authentication and User profile

| Method | Endpoint |
|---------|----------|
| POST | `/users/signup/` |
| POST | `/users/login/` |
| POST | `/users/login/refresh` |
| POST | `/users/logout/` |
| POST | `/users/verify/` |
| GET | `/users/new-verify/` |
| PUT, PATCH | `/users/change-user/` |
| PUT | `/users/change-user-photo/` |
| POST | `/users/forgot-password/` |
| POST | `/users/reset-password/` |



### Posts

| Method | Endpoint |
|---------|----------|
| GET | `/post/posts/` |
| POST | `/post/create/` |
| GET | `/post/<uuid>/` |
| PUT | `/post/<uuid>/` |
| DELETE | `/post/<uuid>/` |
| GET | `/post/<uuid>/likes/` |
| GET | `/post/<uuid>/comments/` |
| PUT | `/post/<uuid>/comments/create/` |
| GET | `/post/comments/` |
| GET | `/post/comments/<uuid>/` |
| GET | `/post/comments/<uuid>/likes` |
| POST | `/post/<uuid:pk>/create-delete-like//` |
| POST | `/post/comments/<uuid:pk>/create-delete-like//` |




### Comments

- Create comment
- Update comment
- Delete comment

### Likes

- Like/Unlike post
- Like/Unlike comment

## Authentication

This project uses JWT Authentication.

Include the access token in every protected request.

```
Authorization: Bearer <access_token>
```

## Environment Variables

The following variables are required:

- SECRET_KEY
- DEBUG
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD

## Future Improvements

- Search users
- Image upload optimization

## License

This project was created for learning and educational purposes.
