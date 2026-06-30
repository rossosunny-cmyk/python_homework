# Домашняя работа №8

Тесты проверяют методы YouGile для работы с проектами:

- `POST /api-v2/projects`;
- `GET /api-v2/projects/{id}`;
- `PUT /api-v2/projects/{id}`.

## Подготовка

Установить зависимости:

```bash
pip install -r 08_lesson/requirements.txt
```

Перед запуском нужно указать переменные окружения:

```text
YOUGILE_BASE_URL=<адрес API>
YOUGILE_TOKEN=<ключ API>
YOUGILE_USER_ID=<id пользователя>
```

В коде нет токенов, паролей и других личных данных.

## Запуск тестов

```bash
pytest 08_lesson
```

## Проверка стиля

```bash
flake8 08_lesson
```
