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
- ⚡ Быстрая загрузка отзывов с использованием Redis-кеширования
- ⛏ PostgreSQL + Alembic для работы с базой данных
- 🚀 Docker + GitHub Actions для деплоя

---

## 🛠️ **Используемые технологии**

**Frontend:**

- HTML, CSS, JavaScript.

**Backend:**

- Python (FastAPI).

- PostgreSQL

- Redis

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
├── alembic                         # Каталог для миграций базы данных
│   ├── env.py                      # Основная конфигурация Alembic
│   ├── README                      # Документация по Alembic (по умолчанию)
│   ├── script.py.mako             # Шаблон для генерации миграций
│   └── versions                   # Папка с версиями миграций
│       └── d98e6bd40d2b_create_comments_table.py   # Скрипт миграции для создания таблицы комментариев
├── alembic.ini                    # Конфигурационный файл Alembic
├── app                            # Основная директория backend-приложения
│   ├── controllers                # Контроллеры (роутеры) FastAPI
│   │   ├── admin_controller.py   # Роуты для загрузки и удаления изображений (админка)
│   │   ├── comment_controller.py # Роуты для комментариев
│   │   ├── __init__.py           # Делает папку модулем Python
│   │   └── root_controller.py    # Роуты для отображения главной страницы
│   ├── database.py               # Подключение к базе данных (Async SQLAlchemy)
│   ├── files.code-workspace      # Конфигурация VS Code рабочего пространства
│   ├── __init__.py               # Делает папку app модулем Python
│   ├── main.py                   # Точка входа приложения FastAPI
│   ├── middleware                # Middleware — заголовки безопасности
│   │   ├── csp_middleware.py     # Устанавливает Content-Security-Policy заголовок
│   │   ├── hsts_middleware.py    # Устанавливает Strict-Transport-Security
│   │   ├── __init__.py           # Делает папку модулем Python
│   │   ├── x_content_type_options_middleware.py  # MIME type защита
│   │   └── x_frame_options_middleware.py         # Защита от Clickjacking (X-Frame-Options)
│   ├── models                    # SQLAlchemy модели БД
│   │   ├── comment.py            # Модель таблицы комментариев
│   │   └── __init__.py           # Делает папку модулем Python
│   ├── schemas                   # Pydantic-схемы для валидации запросов и ответов
│   │   ├── comment.py            # Схемы для комментариев
│   │   └── __init__.py           # Делает папку модулем Python
│   ├── services                  # Бизнес-логика
│   │   ├── comment_service.py    # Сервис для обработки логики комментариев
│   │   └── __init__.py           # Делает папку модулем Python
│   └── utils                     # Вспомогательные функции
│       └── __init__.py           # Пока пусто, подготовка под утилиты
├── docker-compose.yml            # Docker оркестрация (поднимает сервисы: API, БД и т.д.)
├── Dockerfile                    # Сборка образа FastAPI-приложения
├── files.code-workspace          # Дубликат конфигурации VS Code (можно удалить)
├── README.md                     # Документация проекта
├── requirements.txt              # Зависимости Python-пакетов
├── static                        # Статические файлы сайта (CSS, JS, изображения)
│   ├── css
│   │   └── style.css             # Основной файл стилей сайта
│   ├── images                    # Папка с изображениями (портфолио, иконки и пр.)
│   │   ├── about.png             # Картинка страницы "О себе"
│   │   ├── favicon.ico           # Иконка сайта
│   │   ├── home.png              # Картинка главной страницы
│   │   ├── portfolio *.png       # Работы портфолио
│   │   └── preview.jpg           # Превью изображение
│   └── js
│       └── script.js             # JS логика сайта (например, отправка формы)
├── structure.txt                 # Файл, где хранится структура проекта
└── templates                     # HTML-шаблоны для рендеринга страниц
    ├── index-en.html             # Главная страница на английском
    ├── index-ru.html             # Главная страница на русском
    └── index-uz.html             # Главная страница на узбекском


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

**Заметка для проекта:**
✨ TODO: Динамическая галерея для портфолио

📁 Идея:
Сделать раздел "Портфолио" таким, чтобы фото отображались автоматически — на основе файлов, находящихся в static/images/.

🔧 Что нужно будет реализовать:

    Создать API-эндпоинт, который будет возвращать список всех изображений из папки static/images/.

    На фронте (в templates/index-ru.html, index-en.html и т.д.) — динамически рендерить <img src="..."> на основе этого списка.

    (Опционально) Добавить фильтрацию, сортировку, превью и т.д.

    (Опционально) Прикрутить красивую библиотеку отображения, например LightGallery.

📌 Заметка: ты уже реализовал backend-загрузку и удаление фото через /admin, так что 50% работы уже готово 💪
