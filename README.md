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
git clone https://github.com/<your-username>/instagram_clone.git
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

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | `/users/signup/` |
| POST | `/users/login/` |
| POST | `/users/verify/` |
| POST | `/users/token/refresh/` |

### Posts

| Method | Endpoint |
|---------|----------|
| GET | `/post/posts/` |
| POST | `/post/posts/` |
| GET | `/post/posts/<uuid>/` |
| PUT | `/post/posts/<uuid>/` |
| DELETE | `/post/posts/<uuid>/` |

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

- Follow/Unfollow users
- Stories
- Notifications
- Saved posts
- Search users
- Image upload optimization

## License

This project was created for learning and educational purposes.
