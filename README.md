# 💇‍♀️ Irada Shamsi Portfolio Website

## 🌟 **Project Description**

**This project is a portfolio website for a professional hair stylist and colorist with an integrated Telegram bot for collecting client reviews and ratings, as well as a “Likes” system that allows users to visually interact with the portfolio gallery.**
**The project includes an admin panel, a public website, and a Telegram bot that work together as a unified ecosystem.**

**Key website features:**

- Homepage with information about the specialist
- Hidden admin panel for moderating reviews
- “About Me” section with detailed experience and services
- Portfolio gallery with a 💜 Likes system
- Client reviews submitted via Telegram, including ratings and comments
- API support for working with reviews

---

## 🔧 **Main Functionality**

- 🎨 Responsive design (desktop & mobile)
- 🌐 Multilingual support (EN, RU, UZ)
- ⚫ Personalized content (portfolio gallery)
- 💜 Portfolio Like system:
- Users can like photos of works
- Likes are stored on the server and persist after page reload
- Visual effects on tap/click (pulse/flash animation)
- Fully optimized for mobile devices
- 🤖 Telegram bot for collecting reviews & ratings
- 📬 Telegram reviews are integrated directly into the website
- 📝 Review moderation through admin panel
- 🔄 API for managing reviews
- 🚀 Docker + GitHub Actions (CI/CD)
- ⚡ Redis for caching reviews
- 🗄️ PostgreSQL + Alembic for database management

---

## 🛠️ **Tech Stack**

**Frontend:**

- HTML

- CSS (including custom animations for likes ❤️)

- JavaScript (integration with Likes & Reviews API)

- Backend

- Python (FastAPI)

- PostgreSQL

- Redis

- SQLAlchemy + Alembic

- Pydantic

- Jinja2 (HTML templating)

- Uvicorn

- DevOps

- Docker / Docker Compose

- .env + dotenv

- GitHub Actions

- Security

- Middleware:

- HSTS

- X-Frame-Options

- X-Content-Type-Options

- CORS


## 💜 Likes System (Portfolio Likes)

* A new interactive feature allows users to express appreciation for portfolio works.

# Details:

- Likes are stored in the database (portfolio_likes)

- Each portfolio item has a unique data-id

- Synchronization with the backend via /api/likes

- Animated visual feedback (CSS + JS)

- Cookie is used to track already liked items

- Works correctly even after page reload or redeployment


## 🤖 Telegram Bot

**The project includes a Telegram bot that collects user reviews, which are then moderated and published on the website.**

- Aiogram
- FSM (Finite State Machine)
- Docker

---

## 🔐 API Usage

# Available endpoints

# Default

-  * GET /api — API home page

-  * GET / — Website home page

# Admin

-  * GET /admin/login — Login page

-  * POST /admin/login — Login request

-  * GET /admin/logout — Logout

# Telegram Reviews

-  * POST /api/telegram-reviews/ — Add a new review

-  * GET /api/telegram-reviews/ — Get list of reviews

# Admin Panel

-  * GET /admin/reviews/ — Admin reviews page

-  * GET /admin/reviews/list — Get reviews for moderation

-  * POST /admin/reviews/{review_id}/approve — Approve review

-  * DELETE /admin/reviews/clear-all — Delete all reviews

-  * DELETE /admin/reviews/{review_id} — Delete a single review

---

## 🏢 **Project Structure**

```
Irada_Shamsi_WebSite/
.
├── alembic                    # 🗃️ Database migrations (Alembic)
│   ├── env.py                 # ⚙️ Alembic configuration
│   ├── README                 # ℹ️ Alembic info file
│   ├── script.py.mako         # 🧩 Migration template
│   └── versions               # 📁 Versioned migration files
│       ├── 2cb11b9e70b4_add_rating_to_telegram_reviews.py     # 🆙 Added rating to reviews
│       ├── 3bb3623147d3_create_portfolio_likes_table.py       # ❤️ Portfolio likes table
│       ├── b71ac99543ae_create_telegram_reviews_table.py      # 🧱 Telegram reviews table
│       ├── d98e6bd40d2b_create_comments_table.py              # 💬 Comments table
│       └── dac3e4607d2a_fix_telegram_id_to_biginteger.py      # 🔧 Fixed type (BigInteger)
├── alembic.ini                # 🧱 Main Alembic config
├── app                        # 🧠 Backend application (FastAPI)
│   ├── config.py              # ⚙️ Settings / environment variables
│   ├── controllers            # 🎛️ FastAPI routes / controllers
│   │   ├── admin_reviews_controller.py         # 🛡️ Review moderation
│   │   ├── __init__.py                          # 📦
│   │   ├── likes_controller.py                  # ❤️ Likes API
│   │   ├── root_controller.py                   # 🏠 Root / health endpoints
│   │   └── telegram_review_controller.py        # ✉️ Telegram reviews API
│   ├── database.py            # 🐘 PostgreSQL connection (async)
│   ├── database_sync.py       # 🔄 Sync engine (Alembic / scripts)
│   ├── dependencies
│   │   └── admin_auth.py      # 🔐 Depends: admin authentication
│   ├── files.code-workspace   # 💼 VS Code workspace (local)
│   ├── __init__.py            # 📦
│   ├── main.py                # 🚀 FastAPI entry point
│   ├── middleware             # 🧱 Security headers
│   │   ├── csp_middleware.py                    # 🛡️ CSP Policy
│   │   ├── hsts_middleware.py                   # 🛡️ HSTS
│   │   ├── __init__.py                          # 📦
│   │   ├── x_content_type_options_middleware.py # 🛡️ X-Content-Type-Options
│   │   └── x_frame_options_middleware.py        # 🛡️ X-Frame-Options
│   ├── models                 # 🗄️ SQLAlchemy models
│   │   ├── __init__.py                          # 📦
│   │   ├── like.py                               # ❤️ Like model
│   │   └── telegram_review.py                    # 📝 Telegram review model
│   ├── schemas                # 🧾 Pydantic schemas
│   │   ├── __init__.py                          # 📦
│   │   └── telegram_review.py                    # 🧾 Review schemas
│   ├── services               # 🧠 Business logic
│   │   ├── __init__.py                          # 📦
│   │   ├── like_service.py                       # ❤️ Like processing (limits/counts)
│   │   ├── redis_client.py                       # ⚡ Redis client
│   │   └── telegram_review_service.py            # ✉️ Reviews handling
│   └── utils                  # 🧰 Utilities
│       ├── custom_static.py                     # 🗂️ Custom StaticFiles
│       └── __init__.py                          # 📦
├── bot                        # 🤖 Telegram bot (Aiogram)
│   ├── bot_instance.py        # 🤖 Bot initialization
│   ├── config.py              # 🔑 Token / settings
│   ├── Dockerfile             # 🐳 Bot Dockerfile
│   ├── handlers.py            # 🧭 Command / state handlers
│   ├── __init__.py            # 📦
│   ├── main_bot.py            # 🚀 Bot entry point
│   ├── requirements.txt       # 📦 Bot dependencies
│   ├── services
│   │   └── telegram_review_service.py           # ✉️ Send reviews to backend
│   └── states.py              # 🧭 FSM (Aiogram)
├── docker-compose.yml         # 🐳 Orchestration: backend + bot + Redis + Postgres
├── Dockerfile                 # 🐳 Backend Dockerfile
├── files.code-workspace       # 💼 VS Code workspace (root)
├── os                         # 📁 Temporary / misc folder (better to rename/remove)
├── README.md                  # 📚 Project documentation
├── requirements.txt           # 📦 Backend dependencies
├── scripts                    # 🛠️ Service / deploy scripts
│   └── start.sh               # ▶️ Start script (run/migrations/services)
├── static                     # 🌐 Website static assets
│   ├── css
│   │   ├── admin_login.css    # 🎨 Admin login styles
│   │   ├── admin_reviews.css  # 🎨 Moderation styles
│   │   └── style.css          # 🎨 Global styles
│   ├── images
│   │   ├── favicon.ico        # 🧿 Site icon
│   │   └── review_avatars     # 🖼️ User avatars
│   │       └── test.txt       # 🗒️ Placeholder
│   ├── js
│   │   ├── admin_reviews.js   # 🧠 Moderation logic
│   │   └── script.js          # 💻 Global JS
│   ├── robots.txt             # 🤖 Indexing
│   └── sitemap.xml            # 🗺️ Site map (SEO)
├── structure.txt              # 🧱 Project structure snapshot
└── templates                  # 🧩 Jinja2 templates
    ├── admin_login.html       # 🔐 Admin login
    ├── admin_reviews.html     # 🧑‍⚖️ Reviews moderation
    ├── index-en.html          # 🌍 Homepage (EN)
    ├── index-ru.html          # 🇷🇺 Homepage (RU)
    └── index-uz.html          # 🇺🇿 Homepage (UZ)


```

---

## 🔗 Links

- [Website](https://irada-shamsi.com)

- [GitHub Repository](https://github.com/Mr-Shams86/Irada_Shamsi_Website)

- [Telegram Feedback Bot](https://t.me/IradaFeedbackBot)

## 📢 **Contacts**

- **Email**: sammertime763@gmail.com

- **Telegram**: [Mr_Shams_1986](https://t.me/Mr_Shams_1986)

---

## 📚 **License**

- MIT License
