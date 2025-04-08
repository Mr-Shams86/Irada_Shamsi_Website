# Irada Shamsi Portfolio Website

## 🌟 **Описание проекта**

Этот проект представляет собой портфолио веб-сайт профессионального парикмахера-колориста.

**Ключевые функции сайта:**

- Главная страница с информацией о специалисте.
- Раздел "Обо мне" с подробным описанием опыта и услуг.
- Галерея работ (портфолио).
- Раздел отзывов клиентов с комментариями и оценками.
- Поддержка API для работы с отзывами.

---

## 🔧 **Функциональные возможности**

- 🎨 Адаптивный дизайн, поддерживающий мобильные устройства.
- 🏆 Оставление отзывов через веб-интерфейс.
- ⚫ Персонализация содержимого (галерея работ).
- 🔄 API для управления отзывами.
- ⛏ PostgreSQL + Alembic для работы с базой данных
- 🚀 Docker + GitHub Actions для деплоя

---

## 🛠️ **Используемые технологии**

**Frontend:**

- HTML, CSS, JavaScript.

**Backend:**

- Python (FastAPI).

- PostgreSQL

- SQLAlchemy + Alembic

- Pydantic

- Uvicorn

**DevOps:**

- Docker / Docker Compose

- .env + dotenv

- GitHub Actions

**Security:**

- Middleware: HSTS, X-Frame-Options, X-Content-Type-Options

- CORS

---

## 🔒 **Установка и запуск проекта**

Убедитесь, что Docker и Docker Compose установлены

Создайте .env с содержимым:

DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/postgres

Соберите и запустите проект:

docker compose up -d --build

Примените миграции:

docker compose exec backend alembic upgrade head

Откройте сайт:

- Если запускаете **локально**: [http://localhost:8000](http://localhost:8000)
- Если через **Docker** с проброшенным портом: [http://localhost:8001](http://localhost:8001)

### 1. **Клонирование репозитория**

```bash
git clone https://github.com/ваш-репозиторий.git
cd ваш-репозиторий
```

### 2. **Установка зависимостей**

Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate    # Linux/MacOS
venv\Scripts\activate       # Windows
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

### 3. **Запуск приложения**

Запустите сервер FastAPI:

````bash
✅ Вариант 1: Локальный запуск (без Docker)

Запустите сервер FastAPI с автоперезапуском при изменениях:

uvicorn app.main:app --reload --port 8000

Приложение будет доступно по адресу:

    http://127.0.0.1:8000

    Swagger UI: http://127.0.0.1:8000/docs

🐳 Вариант 2: Запуск в Docker

Если используете Docker и в docker-compose.yml указано:

ports:
  - "8001:8000"

Запустите проект с помощью Docker:

docker compose up -d --build

После запуска сайт будет доступен по адресу:

    http://localhost:8001

    Swagger UI: http://localhost:8001/docs

---

## 🔐 **Использование API**

### Доступные эндпоинты:

- **GET /comments**: Возвращает список комментариев.
- **POST /comments**: Добавляет новый комментарий.
- **DELETE /comments**: Удалить все комментарии
- **GET /api**: Главная страница API
- **GET/**: Главная страница

### Пример запроса:

```json
{
  "rating": 5,
  "comment": "Отлично!"
}
````

### Пример ответа:

```json
[
  { "rating": 5, "comment": "Отлично!" },
  { "rating": 4, "comment": "Очень хорошо!" }
]
```

---

## 🏢 **Структура проекта**

```
Irada_Shamsi_WebSite/
.
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── d98e6bd40d2b_create_comments_table.py
├── alembic.ini
├── app
│   ├── controllers
│   │   ├── comment_controller.py
│   │   ├── __init__.py
│   │   └── root_controller.py
│   ├── database.py
│   ├── files.code-workspace
│   ├── __init__.py
│   ├── main.py
│   ├── middleware
│   │   ├── csp_middleware.py
│   │   ├── hsts_middleware.py
│   │   ├── __init__.py
│   │   ├── x_content_type_options_middleware.py
│   │   └── x_frame_options_middleware.py
│   ├── models
│   │   ├── comment.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── comment.py
│   │   └── __init__.py
│   ├── services
│   │   ├── comment_service.py
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── files.code-workspace
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── images
│   │   ├── about.png
│   │   ├── favicon.ico
│   │   ├── home.png
│   │   ├── portfolio 10.png
│   │   ├── portfolio 11.png
│   │   ├── portfolio 13.png
│   │   ├── portfolio 14.png
│   │   ├── portfolio 15.png
│   │   ├── portfolio 16.png
│   │   ├── portfolio 17.png
│   │   ├── portfolio 18.png
│   │   ├── portfolio 19.png
│   │   ├── portfolio 1.png
│   │   ├── portfolio 20.png
│   │   ├── portfolio 21.png
│   │   ├── portfolio 22.png
│   │   ├── portfolio 23.png
│   │   ├── portfolio 24.png
│   │   ├── portfolio 25.png
│   │   ├── portfolio 27.png
│   │   ├── portfolio 28.png
│   │   ├── portfolio 2.png
│   │   ├── portfolio 30.png
│   │   ├── portfolio 31.png
│   │   ├── portfolio 32.png
│   │   ├── portfolio 33.png
│   │   ├── portfolio 34.png
│   │   ├── portfolio 35.png
│   │   ├── portfolio 36.png
│   │   ├── portfolio 37.png
│   │   ├── portfolio 38.png
│   │   ├── portfolio 39.png
│   │   ├── portfolio 3.png
│   │   ├── portfolio 40.png
│   │   ├── portfolio 41.png
│   │   ├── portfolio 42.png
│   │   ├── portfolio 43.png
│   │   ├── portfolio 45.png
│   │   ├── portfolio 47.png
│   │   ├── portfolio 48.png
│   │   ├── portfolio 49.png
│   │   ├── portfolio 4.png
│   │   ├── portfolio 50.png
│   │   ├── portfolio 51.png
│   │   ├── portfolio 52.png
│   │   ├── portfolio 53.png
│   │   ├── portfolio 54.png
│   │   ├── portfolio 55.png
│   │   ├── portfolio 56.png
│   │   ├── portfolio 57.png
│   │   ├── portfolio 58.png
│   │   ├── portfolio 59.png
│   │   ├── portfolio 5.png
│   │   ├── portfolio 60.png
│   │   ├── portfolio 61.png
│   │   ├── portfolio 62.png
│   │   ├── portfolio 63.png
│   │   ├── portfolio 64.png
│   │   ├── portfolio 65.png
│   │   ├── portfolio 66.png
│   │   ├── portfolio 67.png
│   │   ├── portfolio 68.png
│   │   ├── portfolio 69.png
│   │   ├── portfolio 6.png
│   │   ├── portfolio 70.png
│   │   ├── portfolio 71.png
│   │   ├── portfolio 7.png
│   │   ├── portfolio 8.png
│   │   ├── portfolio 9.png
│   │   └── preview.jpg
│   └── js
│       └── script.js
├── structure.txt
└── templates
    ├── index-en.html
    ├── index-ru.html
    └── index-uz.html

14 directories, 105 files
```

---

## 🚨 **Известные проблемы**

1. **CORS-проблемы**: Убедитесь, что `allow_origins` в `main.py` включает ваш локальный адрес.
2. **Ошибка доступа к статическим файлам**: Проверьте правильность пути в `app.mount()`.
3. **Отсутствующие зависимости**: Убедитесь, что все пакеты установлены:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📢 **Контакты**

- **Email**: sammertime763@gmail.com
- **Telegram**: [Mr_Shams_1986](https://t.me/Mr_Shams_1986)

---

## 📚 **Лицензия**

Проект распространяется под лицензией MIT. Ознакомьтесь с файлом LICENSE для деталей.
