import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Динамическое определение пути к базе данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '../comments.db')}"

# Создание двигателя базы данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание базы данных
Base = declarative_base()

# Сессии для взаимодействия с базой
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
