# Incident Tracker API

Микросервис для учёта инцидентов с возможностью создания, просмотра и обновления статусов.

## Технологии

- Python 3.8+
- Django 5.2
- Django REST Framework
- SQLite

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/OllyRaret/Incident-Tracker-API
cd incident_tracker
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

3. Примените миграции:

```bash
python manage.py migrate
```

4. Запустите сервер:

```bash
python manage.py runserver
```

Сервер будет доступен по адресу: http://127.0.0.1:8000/

## API Endpoints

### 1. Получить список инцидентов
**GET** `/api/incidents/`

Параметры запроса:
- `status` - фильтр по статусу
- `source` - фильтр по источнику
- `ordering` - сортировка (`created_at`, `-created_at`)

Пример ответа:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "description": "Самокат не в сети",
            "status": "open",
            "status_display": "Открыт",
            "source": "operator",
            "source_display": "Оператор",
            "created_at": "2025-11-09T14:37:53.454525+03:00",
            "updated_at": "2025-11-09T14:46:28.626536+03:00"
        }
    ]
}
```

### 2. Создать инцидент
**POST** `/api/incidents/`

Тело запроса:
```json
{
    "description": "Точка не отвечает",
    "source": "monitoring"
}
```

### 3. Получить инцидент по ID
**GET** `/api/incidents/{id}/`

### 4. Обновить статус инцидента
**PUT/PATCH** `/api/incidents/{id}/`

Тело запроса:
```json
{
    "status": "in_progress"
}
```

## Статусы инцидентов

- `open` - Открыт
- `in_progress` - В работе  
- `resolved` - Решен
- `closed` - Закрыт
- `cancelled` - Отменен

## Источники инцидентов

- `operator` - Оператор
- `monitoring` - Мониторинг
- `partner` - Партнер
- `system` - Система

## Админка

Доступна по адресу: http://127.0.0.1:8000/admin/

Создайте суперпользователя для доступа:
```bash
python manage.py createsuperuser
```
