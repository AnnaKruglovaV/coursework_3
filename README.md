# Курсовой проект по курсу «Основы backend-разработки»

### Для запуска проекта `main`
### Для запуска тестов 
```bash
pytest --cov
```

### Пример работы программы
```text
19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
нет информации счет/карта -> Счет **8381
21344.35 руб.
```

### Пример выполненных тестов
```text

=================================== test session starts ===================================
platform win32 -- Python 3.11.3, pytest-7.4.4, pluggy-1.4.0
rootdir: C:\Users\Анечка\pythonProject\coursework_3
plugins: cov-4.1.0
collected 15 items

tests\test_operation.py .                                                            [  6%] 
tests\test_utils.py ..............                                                   [100%]

---------- coverage: platform win32, python 3.11.3-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
models\__init__.py                    0      0   100%
models\operation.py                  12      0   100%
tests\__init__.py                     0      0   100%
tests\setting_test_operation.py       2      0   100%
tests\test_operation.py              11      0   100%
tests\test_utils.py                  28      0   100%
utils.py                             31      0   100%
-----------------------------------------------------
TOTAL                                84      0   100%

```

# Код для виджета «Операции по счетам»

<aside>
👨🏻‍💻 IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. Вам доверили реализовать алгоритм, который на бэкенде будет готовить данные для отображения в новом виджете.

</aside>

## Задача

Реализуйте функцию, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:

<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>

```bash
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```

### Требования

- Последние 5 выполненных (EXECUTED) операций выведены на экран.
- Операции разделены пустой строкой.
- Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
- Сверху списка находятся самые последние операции (по дате).
- Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
- Номер счета замаскирован и не отображается целиком в формате  **XXXX 
(видны только последние 4 цифры номера счета).

## Данные

Файл со списком операций, совершенных клиентом банка:

[operations.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dd686a1e-f5aa-4c73-b4f2-163a93b8432b/operations.zip)

<aside>
💡 Скачайте файл и положите его в проект. Работать с ним надо через библиотеку json. Файл модифицировать нельзя. Все нестандартные записи обрабатывать программно.

</aside>

По каждой операции есть следующие данные:

- `id` — id транзакциии
- `date` — информация о дате совершения операции
- `state` — статус перевода:
    - `EXECUTED`  — выполнена,
    - `CANCELED`  — отменена.
- `operationAmount` — сумма операции и валюта
- `description` — описание типа перевода
- `from` — откуда (может отсутстовать)
- `to` — куда

## Критерии выполнения

- [ ]  Проект выложили на GitHub.
- [ ]  Есть файл .gitignore
- [ ]  Оформили файл README.md.
- [ ]  В проекте есть минимум 2 ветки, причем разработка ведется в `develop`, а стабильная версия на момент сдачи проекта лежит в ветке `main`.
- [ ]  Разработка проекта ведется в виртуальном окружении, в проекте есть информация о требованиях проекта (зависимостях).
- [ ]  К проекту написали тесты с покрытием не менее 80%.
- [ ]  Тесты написали на `pytest` или `unittest`.
- [ ]  Проект структурированный, читаемый, каждая функция — не более 50 строк.
- [ ]  Работа с файлом ведется через библиотеку json