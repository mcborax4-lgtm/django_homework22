# Django Catalog Project

Учебный проект на Django — сайт с главной страницей и страницей контактов.

## Технологии
- Python 3.13
- Django 6.0.4
- Bootstrap 5

## Установка и запуск
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## Структура проекта
- `catalog/` — приложение с контроллерами и маршрутами
- `templates/` — HTML шаблоны
- `config/` — настройки проекта

## Ветки (GitFlow)
- `main` — стабильный код
- `develop` — разработка
- `homework/task-XX` — ветки для каждого задания

## База данных
Проект использует PostgreSQL. Создай файл `.env` в папке `django_project`:
```DB_NAME=django_homework
DB_USER=postgres
DB_PASSWORD=твой_пароль
DB_HOST=localhost
DB_PORT=5432
```
## Заполнение базы тестовыми данными
```bash
python manage.py fill_db
```