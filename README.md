# Irada Shamsi Portfolio Website

## 🌟 **Описание проекта**

**Этот проект представляет собой портфолио веб-сайт профессионального парикмахера-колориста с интеграцией Telegram-бота для оценок и сбора отзывов клиентов, а также системой лайков для визуального взаимодействия пользователей с галереей работ.**
**Проект включает административную панель, публичный сайт и Telegram-бот, работающие как единая экосистема.**

**Ключевые функции сайта:**

- Главная страница с информацией о специалисте.
- Скрытая Админ панель для модерации отзывов
- Раздел "Обо мне" с подробным описанием опыта и услуг.
- Галерея работ (портфолио) с системой лайков 💜.
- Раздел отзывов клиентов через Telegram с оценками и комментариями.
- Поддержка API для работы с отзывами.

---

## 🔧 **Функциональные возможности**

- 🎨 Адаптивный дизайн (desktop/mobile)
- 🌐 Многоязычная поддержка (EN, RU, UZ)
- ⚫ Персонализация содержимого (галерея работ)
- 💜 Система лайков для портфолио:
-    Пользователи могут ставить лайки к фото работ.
-    Лайки сохраняются на сервере и остаются при обновлении страницы.
-    Визуальные эффекты при нажатии (анимация "вспышки").
-    Кнопка адаптируется под мобильные устройства.
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

- HTML

- CSS (включая кастомные анимации для лайков ❤️)

- JavaScript (взаимодействие с API лайков и отзывов)

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

- Middleware: HSTS

- X-Frame-Options

- X-Content-Type-Options

- CORS

## 💜 Система лайков (Portfolio Likes)

- Добавлена новая интерактивная функция, позволяющая пользователям выражать одобрение понравившимся работам.
- Особенности:

- Лайки сохраняются в базе данных (portfolio_likes);

- Каждый элемент портфолио имеет уникальный data-id;

- Поддерживается синхронизация с сервером через /api/likes;

- Реализованы анимации и визуальные эффекты (CSS + JS);

- Cookie фиксирует, какие работы уже лайкнуты пользователем;

- Работает стабильно даже после редеплоя и обновления страницы.

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
├── alembic                    # 🗃️ Миграции базы данных (Alembic)
│   ├── env.py                 # ⚙️ Конфигурация Alembic
│   ├── README                 # ℹ️ Инфо-файл Alembic
│   ├── script.py.mako         # 🧩 Шаблон миграций
│   └── versions               # 📁 Файлы миграций по версиям
│       ├── 2cb11b9e70b4_добавил_рейтинг_в_telegram_reviews.py   # 🆙 Добавлен рейтинг к отзывам
│       ├── 3bb3623147d3_create_portfolio_likes_table.py        # ❤️ Таблица лайков портфолио
│       ├── b71ac99543ae_create_telegram_reviews_table.py       # 🧱 Таблица telegram-отзывов
│       ├── d98e6bd40d2b_create_comments_table.py               # 💬 Таблица комментариев
│       └── dac3e4607d2a_fix_telegram_id_to_biginteger.py       # 🔧 Исправление типа (BigInteger)
├── alembic.ini                # 🧱 Основной конфиг Alembic
├── app                        # 🧠 Backend-приложение (FastAPI)
│   ├── config.py              # ⚙️ Настройки/переменные окружения
│   ├── controllers            # 🎛️ Роуты/контроллеры FastAPI
│   │   ├── admin_reviews_controller.py         # 🛡️ Модерация отзывов
│   │   ├── __init__.py                          # 📦
│   │   ├── likes_controller.py                  # ❤️ API лайков
│   │   ├── root_controller.py                   # 🏠 Корневые/health endpoints
│   │   └── telegram_review_controller.py        # ✉️ API отзывов из Telegram
│   ├── database.py            # 🐘 Подключение к PostgreSQL (async)
│   ├── database_sync.py       # 🔄 Синхронный движок (Alembic/скрипты)
│   ├── dependencies
│   │   └── admin_auth.py      # 🔐 Depends: админ-аутентификация
│   ├── files.code-workspace   # 💼 Workspace VS Code (локально)
│   ├── __init__.py            # 📦
│   ├── main.py                # 🚀 Точка входа FastAPI
│   ├── middleware             # 🧱 Заголовки безопасности
│   │   ├── csp_middleware.py                    # 🛡️ CSP Policy
│   │   ├── hsts_middleware.py                   # 🛡️ HSTS
│   │   ├── __init__.py                          # 📦
│   │   ├── x_content_type_options_middleware.py # 🛡️ X-Content-Type-Options
│   │   └── x_frame_options_middleware.py        # 🛡️ X-Frame-Options
│   ├── models                 # 🗄️ SQLAlchemy-модели
│   │   ├── __init__.py                          # 📦
│   │   ├── like.py                               # ❤️ Модель лайка
│   │   └── telegram_review.py                    # 📝 Модель телеграм-отзыва
│   ├── schemas                # 🧾 Pydantic-схемы
│   │   ├── __init__.py                          # 📦
│   │   └── telegram_review.py                    # 🧾 Схемы отзывов
│   ├── services               # 🧠 Бизнес-логика
│   │   ├── __init__.py                          # 📦
│   │   ├── like_service.py                       # ❤️ Работа с лайками (ограничения/подсчёт)
│   │   ├── redis_client.py                       # ⚡ Клиент Redis
│   │   └── telegram_review_service.py            # ✉️ Обработка отзывов
│   └── utils                  # 🧰 Утилиты
│       ├── custom_static.py                     # 🗂️ Кастомный StaticFiles
│       └── __init__.py                          # 📦
├── bot                        # 🤖 Telegram-бот (Aiogram)
│   ├── bot_instance.py        # 🤖 Инициализация бота
│   ├── config.py              # 🔑 Токен/настройки
│   ├── Dockerfile             # 🐳 Dockerfile бота
│   ├── handlers.py            # 🧭 Хендлеры команд/состояний
│   ├── __init__.py            # 📦
│   ├── main_bot.py            # 🚀 Точка входа бота
│   ├── requirements.txt       # 📦 Зависимости бота
│   ├── services
│   │   └── telegram_review_service.py           # ✉️ Отправка отзывов на backend
│   └── states.py              # 🧭 FSM (Aiogram)
├── docker-compose.yml         # 🐳 Оркестрация: backend + bot + Redis + Postgres
├── Dockerfile                 # 🐳 Dockerfile backend
├── files.code-workspace       # 💼 Workspace VS Code (корень)
├── os                         # 📁 Временная/прочая папка (лучше переименовать/убрать)
├── README.md                  # 📚 Документация проекта
├── requirements.txt           # 📦 Зависимости backend
├── scripts                    # 🛠️ Скрипты обслуживания/деплоя
│   └── start.sh               # ▶️ Стартовый скрипт (запуск/миграции/службы)
├── static                     # 🌐 Статические ресурсы сайта
│   ├── css
│   │   ├── admin_login.css    # 🎨 Стили входа админа
│   │   ├── admin_reviews.css  # 🎨 Стили модерации
│   │   └── style.css          # 🎨 Общие стили
│   ├── images
│   │   ├── favicon.ico        # 🧿 Иконка сайта
│   │   └── review_avatars     # 🖼️ Аватарки пользователей
│   │       └── test.txt       # 🗒️ Заглушка
│   ├── js
│   │   ├── admin_reviews.js   # 🧠 Логика модерации
│   │   └── script.js          # 💻 Общий JS
│   ├── robots.txt             # 🤖 Индексация
│   └── sitemap.xml            # 🗺️ Карта сайта (SEO)
├── structure.txt              # 🧱 Снимок структуры проекта
└── templates                  # 🧩 Jinja2-шаблоны
    ├── admin_login.html       # 🔐 Вход в админку
    ├── admin_reviews.html     # 🧑‍⚖️ Модерация отзывов
    ├── index-en.html          # 🌍 Главная (англ.)
    ├── index-ru.html          # 🇷🇺 Главная (рус.)
    └── index-uz.html          # 🇺🇿 Главная (узб.)



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
