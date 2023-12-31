[![All](https://github.com/karbolinivan/QACloudCamp/actions/workflows/all.yml/badge.svg)](https://karbolinivan.github.io/QACloudCamp/all)
[![smoke](https://github.com/karbolinivan/QACloudCamp/actions/workflows/smoke.yml/badge.svg)](https://karbolinivan.github.io/QACloudCamp/smoke)
[![regression](https://github.com/karbolinivan/QACloudCamp/actions/workflows/regression.yml/badge.svg)](https://karbolinivan.github.io/QACloudCamp/regression)  
# QACloudCamp
<img src="https://img.shields.io/badge/python-0d1117?style=for-the-badge&logo=python"><img src="https://img.shields.io/badge/pytest-0d1117?style=for-the-badge&logo=pytest"><img src="https://img.shields.io/badge/pydantic-0d1117?style=for-the-badge&logo=pydantic"><img src="https://img.shields.io/badge/docker-0d1117?style=for-the-badge&logo=docker"><img src="https://img.shields.io/badge/Actions-0d1117?style=for-the-badge&logo=githubactions"><img src="https://img.shields.io/badge/pycharm-0d1117?style=for-the-badge&logo=pycharm&logoColor=0"><img src="https://img.shields.io/badge/git-0d1117?style=for-the-badge&logo=git&logoColor=0"><img src="https://img.shields.io/badge/github-0d1117?style=for-the-badge&logo=github">


# Задание 1

## Стратегия тестирования

### Функциональность:

Создание пользовательской базы данных через веб-интерфейс.

### Критерии начала тестирования:

1. Определены требования.
2. Подготовлена тестовая документация.
3. Подготовлена тестовая БД.
4. Подготовлен тестовый сервис (frontend, backend).

### Критерии окончания тестирования:

1. Проведены все тестовые сценарии.
2. Выявлены, локализованы, задокументированы и устранены ошибки.
3. Составлен отчет о тестировании.

### Окружение:

1. Операционная система: Windows 10, MacOS Catalina, Android 11, iOS 16.
2. Браузеры: Chrome, Firefox, Safari, Opera.
3. База данных: PostgreSQL.

### Smoke тесты:

1. Проверка работы страницы.
2. Проверка кнопки «Создать», обязательных полей и валидации.
3. Проверка создания пользовательской базы данных.
4. Проверка возможности подключения пользователя к базе данных.

### Функциональное тестирование:

Тестирование Веб:

1. Проверка создания/удаления пользовательской базы данных.
2. Проверка добавления/изменения/удаления данных.
3. Проверка создания базы данных используя различные варианты полей регион размещения и размер.
4. Проверка создания пользователем двух и более баз данных.

Тестирование API:

1. Проверка создание/удаления базы данных используя API.
2. Проверка добавления/изменения/удаления данных API.
3. Проверка валидации данных между API/БД.

Тестирование БД:

1. Созданная база данных соответствует запросу пользователя (название, регион, размер).
2. Все поля, созданные пользователем, присутствуют.
3. Поля имеют тип данных и ограничения в соответствии с запросом пользователя.
4. Данные, добавленные в базу данных, совпадают с данными, переданными пользователем.
5. Выдача информации по запросу пользователя соответствует ожидаемому результату.

### Нефункциональное тестирование:

Производительность:

1. Проверка скорости создания/удаления пользовательской базы данных.
2. Проверка скорости работы базы данных при добавлении/удалении/изменении данных.
3. Проверка скорости работы базы данных используя различные регионы и размер.

Тестирование UI:

1. Отображение страницы и элементов в соответствии с макетом.
2. Отображение обязательных полей.
3. Отображение сообщения об ошибки при отсутствии или вводе невалидных данных в обязательные поля.

Тестирование безопасности:

1. Проверка доступа к базе данных через веб-интерфейс.
2. Проверка доступа к базе данных через API.
3. Проверка доступа к базе данных напрямую в БД.

### Кроссбраузерное тестирование:

1. На всех выбранных браузерах страница отображается в соответствии с макетом.
2. Адаптивная версия сайта для мобильных устройств отображается в соответствии с макетом.

***

# Задание 2

## Docker-compose

### Запуск

```
docker-compose up
```
1. Сборка контейнера
2. Запуск автотестов
3. Сохранение отчета Allure на хост системе

### Запуск отчета Allure:

```
allure serve allure_reports
```

### Остановка

```
docker-compose down
```

---

## Дополнительные команды

## Сборка Docker контейнера

### Сборка

```
docker build -t automation:1.0 .
```

### Сборка smoke/regression тестов

```
docker build --build-arg run_env=smoke -t automation:1.0 .
```

### Запуск

```
docker run automation:1.0
```

### ID контейнера

```
docker ps -a
```

### Получение отчетов Allure из контейнера

```
docker cp "id_контейнера":./usr/project/allure_reports .
```

## Настройка

### Окружение

```
python3 -m venv venv source venv/bin/activate
```

### Зависимости

```
pip3 install -r requirements.txt
```

## Тесты

### Запуск автотестов:

```
python -m pytest -s -v
```

### Запуск автотестов с сохранением отчета Allure:

```
python -m pytest --alluredir=allure_reports
```
