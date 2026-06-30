# Домашняя работа №9

Тесты проверяют работу с сущностью `student` через SQLAlchemy:

- добавление записи;
- изменение записи;
- удаление записи.

Для тестов используется отдельная таблица `lesson9_students`.

## Подготовка

Установить зависимости:

```bash
pip install -r 09_lesson/requirements.txt
```

Перед запуском нужно указать переменную окружения `DATABASE_URL` со строкой подключения к PostgreSQL:

```text
postgresql://user:password@host:port/database
```

## Запуск тестов

```bash
pytest 09_lesson
```

## Проверка стиля

```bash
flake8 09_lesson
```
