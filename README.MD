# QACloudCamp

## Docker

### Сборка

```Python
docker build -t automation:1.0 .
```

### Сборка smoke/regression тестов

```Python
docker build --build-arg run_env=smoke -t automation .
```

### Запуск

```Python
docker run -d automation
```

### ID контейнера

```Python
docker ps -a
```

### Получение отчетов Allure из контейнера

```
docker cp "id_контейнера":./usr/project/allure_reports .
```

### Запуск отчета Allure:

```Python
allure serve allure_reports
```

## Настройка

### Окружение

```Python
python3 -m venv venv source venv/bin/activate
```

### Зависимости

```Python
pip3 install -r requirements.txt
```

## Тесты

### Запуск автотестов:

```Python
python -m pytest -s -v
```

### Запуск автотестов с сохранением отчета Allure:

```Python
python -m pytest --alluredir=allure_reports
```
