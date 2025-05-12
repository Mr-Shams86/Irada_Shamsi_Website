# Irada Shamsi Portfolio Website

## 🌟 **Описание проекта**

**Этот проект представляет собой портфолио веб-сайт профессионального парикмахера-колориста с интеграцией Telegram-бота для оценок и сбора отзывов клиентов.**
**Проект включает административную панель, публичный сайт и Telegram-бот, работающие как единая экосистема.**

**Ключевые функции сайта:**

- Главная страница с информацией о специалисте.
- Скрытая Админ панель для модерации отзывов
- Раздел "Обо мне" с подробным описанием опыта и услуг.
- Галерея работ (портфолио).
- Раздел отзывов клиентов через Telegram с оценками и комментариями.
- Поддержка API для работы с отзывами.

---

## 🔧 **Функциональные возможности**

- 🎨 Адаптивный дизайн (desktop/mobile)
- 🌐 Многоязычная поддержка (EN, RU, UZ)
- ⚫ Персонализация содержимого (галерея работ)
- 🤖 Telegram-бот для сбора отзывов и оценок от клиентов
- 📬 Интеграция отзывов Telegram прямо на сайт
- 📝 Модерация отзывов через admin-панель
- 🔄 API для управления отзывами
- 🚀 Docker + GitHub Actions для CI/CD
- ⚡ Redis для кеширования отзывов
- 🗄️ PostgreSQL + Alembic для базы данных

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

- Jinja2 (шаблонизатор для HTML)

- Uvicorn

**DevOps:**

- Docker / Docker Compose

- .env + dotenv

- GitHub Actions

**Security:**

- Middleware: HSTS, X-Frame-Options, X-Content-Type-Options

- CORS

## 🤖 Telegram-бот

**В проект входит Telegram-бот для сбора отзывов пользователей с последующей модерацией и публикацией на сайте.**

- Aiogram
- FSM (машина состояний)
- Docker

---

## 🔐 **Использование API**

### Доступные эндпоинты:

- default:
- **GET /api**: Главная страница API
- **GET/**: Главная страница

- Admin:
- **GET/admin/login**: Login Get
- **POST/admin/login**: Login Post
- **GET/admin/logout**: Logout

- Telegram Reviews
- **POST/api/telegram-reviews/**: Add Review
- **GET/api/telegram-reviews/**: List Review

- Admin Panel:
- **GET/admin/reviews/**:
- **GET/admin/reviews/list**: Get Reviews For Moderation:
- **POST/admin/reviews/{review_id}/approve**: Approve Review:
- **DELETE/admin/reviews/clear-all**: Delete all Review:
- **DELETE/admin/reviews/{review_id}**: Delete Review:

---

## 🏢 **Структура проекта**

```
Irada_Shamsi_WebSite/
.
├── alembic                             # 📂 Миграции базы данных (Alembic)
│   ├── env.py                          # ⚙️ Конфигурация Alembic
│   ├── README                          # 📝 Инфо-файл Alembic
│   ├── script.py.mako                  # 🧩 Шаблон миграции
│   └── versions                        # 📂 Файлы миграций по версиям
│       ├── 2cb11b9e70b4_добавил_рейтинг_в_telegram_reviews.py   # ➕ Миграция: добавлен рейтинг
│       ├── b71ac99543ae_create_telegram_reviews_table.py        # 🆕 Миграция: таблица отзывов Telegram
│       ├── d98e6bd40d2b_create_comments_table.py                # 🆕 Миграция: таблица комментариев
│       └── dac3e4607d2a_fix_telegram_id_to_biginteger.py        # 🛠️ Миграция: исправление типа telegram_id
├── alembic.ini                        # ⚙️ Основной конфиг Alembic
├── app                                # 📂 Backend-приложение (FastAPI)
│   ├── config.py                      # ⚙️ Конфигурация проекта (переменные окружения и пути)
│   ├── controllers                    # 📂 Контроллеры/роуты FastAPI
│   │   ├── admin_reviews_controller.py    # 🔐 Роуты для админки модерации отзывов
│   │   ├── __init__.py                    # 📦 Модуль init
│   │   ├── root_controller.py             # 🏠 Главная страница сайта
│   │   └── telegram_review_controller.py  # 📬 Роуты API для отзывов из Telegram
│   ├── database.py                   # 🛢️ Асинхронное подключение к PostgreSQL
│   ├── database_sync.py              # 🔁 Синхронное подключение для Alembic миграций
│   ├── dependencies                  # 📂 Зависимости проекта (например, авторизация)
│   │   └── admin_auth.py             # 🔐 Базовая админ-аутентификация
│   ├── files.code-workspace          # 📝 Файл рабочего пространства VS Code
│   ├── __init__.py                   # 📦 Модуль инициализации приложения
│   ├── main.py                       # 🚀 Точка запуска FastAPI-приложения
│   ├── middleware                    # 📂 Middleware для заголовков безопасности
│   │   ├── csp_middleware.py         # 🔒 CSP — Content Security Policy
│   │   ├── hsts_middleware.py        # 🔒 HSTS — HTTPS Strict Transport Security
│   │   ├── __init__.py               # 📦 Модуль
│   │   ├── x_content_type_options_middleware.py  # 🔐 X-Content-Type-Options заголовок
│   │   └── x_frame_options_middleware.py         # 🔐 X-Frame-Options защита
│   ├── models                        # 📂 SQLAlchemy модели
│   │   ├── __init__.py               # 📦 Модуль
│   │   └── telegram_review.py        # 🗄️ Модель таблицы отзывов из Telegram
│   ├── schemas                       # 📂 Pydantic-схемы
│   │   ├── __init__.py               # 📦 Модуль
│   │   └── telegram_review.py        # 📄 Схемы сериализации отзывов
│   ├── services                      # 📂 Бизнес-логика
│   │   ├── __init__.py               # 📦 Модуль
│   │   ├── redis_client.py           # 🧠 Клиент Redis
│   │   └── telegram_review_service.py# 🧠 Логика обработки Telegram-отзывов
│   └── utils                         # 📂 Вспомогательные утилиты
│       ├── custom_static.py          # 📁 Кастомный static-файл обработчик
│       └── __init__.py               # 📦 Модуль
├── bot                                # 🤖 Папка Telegram-бота
│   ├── bot_instance.py                # 🤖 Создание экземпляра бота (Aiogram)
│   ├── config.py                      # ⚙️ Токен бота и BACKEND_URL
│   ├── Dockerfile                     # 🐳 Dockerfile для Telegram-бота
│   ├── handlers.py                    # 📬 Обработчики команд/состояний
│   ├── __init__.py                    # 📦 Модуль
│   ├── main_bot.py                    # 🚀 Точка входа Telegram-бота
│   ├── requirements.txt              # 📦 Зависимости бота
│   ├── services
│   │   └── telegram_review_service.py # 🔁 Отправка отзывов с бота на backend
│   └── states.py                      # 🧭 FSM-состояния (Aiogram FSMContext)
├── docker-compose.yml                 # ⚙️ Docker-оркестрация (backend + bot + Redis + DB)
├── Dockerfile                         # 🐳 Dockerfile для backend (FastAPI)
├── files.code-workspace               # 📝 VS Code workspace (повтор)
├── os                                 # ⚠️ Возможно, временная/тестовая папка
├── README.md                          # 📘 Документация проекта
├── requirements.txt                   # 📦 Зависимости для FastAPI-приложения
├── static                             # 📂 Статические ресурсы для сайта
│   ├── css
│   │   ├── admin_login.css            # 🎨 Стили страницы входа админа
│   │   ├── admin_reviews.css          # 🎨 Стили админки модерации
│   │   └── style.css                  # 🎨 Общие стили сайта
│   ├── images
│   │   └── review_avatars             # 🖼️ Аватарки пользователей Telegram
│   │       └── test.txt               # 📄 Временный/заглушка-файл
│   ├── js
│   │   ├── admin_reviews.js           # 🧠 JS-логика модерации отзывов
│   │   └── script.js                  # 💡 Основной JS для сайта
│   ├── robots.txt                     # 🤖 SEO-файл для запрета/разрешения индексации
│   └── sitemap.xml                    # 🗺️ Карта сайта (SEO)
├── structure.txt                      # 📄 Файл со структурой проекта (этот)
└── templates                          # 📂 HTML-шаблоны (Jinja2)
    ├── admin_login.html               # 🔐 Страница входа в админку
    ├── admin_reviews.html             # 📝 Интерфейс модерации отзывов
    ├── index-en.html                  # 🌐 Главная страница (англ.)
    ├── index-ru.html                  # 🌐 Главная страница (рус.)
    └── index-uz.html                  # 🌐 Главная страница (узбек.)


```

---

## 🔗 Ссылки

- [Сайт проекта](https://irada-shamsi.com)
- [GitHub репозиторий](https://github.com/Mr-Shams86/Irada_Shamsi_Website)
- [Telegram-бот для отзывов](https://t.me/IradaFeedbackBot)

## 📢 **Контакты**

- **Email**: sammertime763@gmail.com
- **Telegram**: [Mr_Shams_1986](https://t.me/Mr_Shams_1986)

---

## 📚 **Лицензия**

- MIT License
