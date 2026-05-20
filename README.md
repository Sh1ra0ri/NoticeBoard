# Notice Board

## 📌 Описание проекта

Notice Board — backend-приложение для сайта объявлений.
Пользователи могут создавать объявления, редактировать их, удалять и оставлять отзывы.

---

## 📥 Клонирование репозитория

```bash id="c1"
git clone https://github.com/Sh1ra0ri/NoticeBoard.git
cd notice-board
```
---

## ⚙️ Технологии

* Python
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* django-filter
* Docker

---

## 🚀 Запуск через Docker

```bash id="c2"
docker-compose up --build
```

---

## 🧪 Локальный запуск

```bash id="c3"
python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 👤 Создание суперпользователя

```bash id="c4"
python manage.py createsuperuser
```

---

## 🔐 Авторизация

### Получение токена

POST `/token/`

```json id="c5"
{
  "email": "user@mail.com",
  "password": "password"
}
```

---

## 📧 Восстановление пароля

### Запрос

POST `/users/reset_password/`

```json id="c6"
{
  "email": "user@mail.com"
}
```

### Подтверждение

POST `/users/reset_password_confirm/`

```json id="c7"
{
  "uid": "uid",
  "token": "token",
  "new_password": "new_password"
}
```

---

## 📦 Объявления

* GET `/ads/` — список
* POST `/ads/` — создать
* GET `/ads/{id}/` — получить
* PUT `/ads/{id}/` — обновить
* DELETE `/ads/{id}/` — удалить

---

## 🔍 Поиск

```
/ads/?title=example
```

---

## 📄 Пагинация

```
/ads/?page=1
```

---

## 📚 Документация

* Swagger: `/swagger/`
* Redoc: `/redoc/`

---

## 🌐 Доступ

* http://127.0.0.1:8000
* PostgreSQL: localhost:5432

---
