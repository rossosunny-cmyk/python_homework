# Домашняя работа №10

Проект содержит UI-тесты из домашней работы №7, оформленные с использованием Page Object и Allure.

## Что проверяют тесты

- `test_01_calc.py` — проверка калькулятора.
- `test_02_shop.py` — проверка покупки в интернет-магазине.

## Установка зависимостей

```bash
pip install -r 10_lesson/requirements.txt
```

## Запуск тестов с формированием Allure-результатов

```bash
pytest 10_lesson --alluredir=10_lesson/allure-results
```

## Просмотр Allure-отчета

```bash
allure serve 10_lesson/allure-results
```

## Проверка стиля

```bash
flake8 10_lesson
```
