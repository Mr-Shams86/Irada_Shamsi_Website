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
├── alembic                           # 📂 Папка миграций базы данных (Alembic)
│   ├── env.py                        # ⚙️ Конфигурация Alembic
│   ├── README                        # 📝 Документация Alembic
│   ├── script.py.mako                # 🧩 Шаблон для генерации миграций
│   └── versions                      # 📂 Файлы миграций версий базы данных
│       ├── 2cb11b9e70b4_добавил_рейтинг_в_telegram_reviews.py  # ➕ Миграция: добавлен рейтинг
│       ├── b71ac99543ae_create_telegram_reviews_table.py       # ➕ Миграция: создана таблица telegram_reviews
│       ├── d98e6bd40d2b_create_comments_table.py               # ➕ Миграция: создана таблица comments
│       └── dac3e4607d2a_fix_telegram_id_to_biginteger.py      # 🛠️ Миграция: изменён тип telegram_id
├── alembic.ini                      # ⚙️ Конфигурационный файл Alembic
├── app                              # 📂 Папка backend-приложения
│   ├── config.py                    # ⚙️ Конфиг проекта (настройки, env)
│   ├── controllers                  # 📂 Контроллеры FastAPI (роутеры)
│   │   ├── admin_reviews_controller.py  # 🔐 Роуты админки модерации отзывов
│   │   ├── __init__.py              # 📦 Делает папку модулем Python
│   │   ├── root_controller.py       # 🏠 Роут главной страницы сайта
│   │   └── telegram_review_controller.py  # 📬 Роуты работы с Telegram-отзывами
│   ├── database.py                  # 🛢️ Подключение к БД (асинхронное)
│   ├── database_sync.py             # 🛢️ Подключение для Alembic (синхронное)
│   ├── dependencies                 # 📂 Зависимости проекта
│   │   └── admin_auth.py            # 🔐 Аутентификация админа
│   ├── files.code-workspace         # 📝
│   ├── __init__.py                  # 📦 Делает app модулем Python
│   ├── main.py                      # 🚀 Точка входа FastAPI
│   ├── middleware                   # 📂 Middleware (промежуточные обработки)
│   │   ├── csp_middleware.py        # 🔒 CSP заголовки
│   │   ├── hsts_middleware.py       # 🔒 HSTS заголовки
│   │   ├── __init__.py              # 📦 Делает папку модулем
│   │   ├── x_content_type_options_middleware.py  # 🔒 X-Content-Type-Options заголовок
│   │   └── x_frame_options_middleware.py         # 🔒 X-Frame-Options заголовок
│   ├── models                       # 📂 SQLAlchemy модели
│   │   ├── __init__.py              # 📦 Делает папку модулем
│   │   └── telegram_review.py       # 🗄️ Модель таблицы telegram_reviews
│   ├── schemas                      # 📂 Pydantic-схемы
│   │   ├── __init__.py              # 📦 Делает папку модулем
│   │   └── telegram_review.py       # 📄 Схемы для telegram_reviews
│   ├── services                     # 📂 Бизнес-логика
│   │   ├── __init__.py              # 📦 Делает папку модулем
│   │   ├── redis_client.py          # 🗃️ Подключение к Redis
│   │   └── telegram_review_service.py  # 🧠 Логика работы с отзывами Telegram
│   └── utils                        # 📂 Вспомогательные утилиты
│       ├── custom_static.py         # 📝 Кастомный static-файл обработчик
│       └── __init__.py              # 📦 Делает папку модулем
├── bot                              # 🤖 Папка с Telegram-ботом
│   ├── bot_instance.py              # 🤖 Экземпляр бота Aiogram
│   ├── config.py                    # ⚙️ Конфиг бота (токен, URL)
│   ├── Dockerfile                   # 🐳 Dockerfile для контейнера бота
│   ├── handlers.py                  # 📬 Обработчики команд бота
│   ├── __init__.py                  # 📦 Делает папку модулем
│   ├── main_bot.py                  # 🚀 Точка входа Telegram-бота
│   ├── requirements.txt             # 📦 Зависимости бота
│   └── states.py                    # 🧭 Состояния FSM (машина состояний) бота
├── docker-compose.yml               # ⚙️ Docker-оркестрация проекта
├── Dockerfile                       # 🐳 Dockerfile для backend-приложения
├── files.code-workspace             # 📝
├── os                               # ⚠️
├── README.md                        # 📝 Документация проекта
├── requirements.txt                 # 📦 Зависимости backend-приложения
├── static                           # 📂 Статические файлы сайта
│   ├── css
│   │   ├── admin_login.css          # 🎨 Стили страницы логина админки
│   │   ├── admin_reviews.css        # 🎨 Стили админки модерации отзывов
│   │   └── style.css                # 🎨 Основные стили сайта
│   ├── images                       # 📂 Изображения сайта
│   ├── js
│   │   ├── admin_reviews.js         # 📜 Логика JS для админки отзывов
│   │   └── script.js                # 📜 Основной JS-файл сайта
│   ├── robots.txt                   # 🤖 robots.txt (SEO-файл для поисковиков)
│   └── sitemap.xml                  # 🗺️ Sitemap.xml (карта сайта для поисковиков)
├── structure.txt                    # 📄 Файл структуры проекта
└── templates                        # 📂 HTML-шаблоны
    ├── admin_login.html             # 📝 Шаблон страницы логина админки
    ├── admin_reviews.html           # 📝 Шаблон админки модерации отзывов
    ├── index-en.html                # 🏠 Главная страница (английская)
    ├── index-ru.html                # 🏠 Главная страница (русская)
    └── index-uz.html                # 🏠 Главная страница (узбекская)

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
