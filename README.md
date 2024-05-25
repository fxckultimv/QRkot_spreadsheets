# QRKot - приложение для поддержки котиков

### Готовый API для благотворительных проектов: создавайте проекты для сбора средств и регистрируйте поступающие пожертвования.

[![FastAPI](https://img.shields.io/badge/FastAPI-%23FF3535.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-%23FFFFFF.svg?style=for-the-badge&logo=uvicorn&logoColor=black)](https://www.uvicorn.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-%23FF3535.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Python](https://img.shields.io/badge/Python-%23FFFFFF.svg?style=for-the-badge&logo=python&logoColor=black)](https://www.python.org/)
[![JWT Token](https://img.shields.io/badge/JWT%20Token-%23FF3535.svg?style=for-the-badge&logo=jwt&logoColor=white)](https://jwt.io/)
[![Alembic](https://img.shields.io/badge/Alembic-%23FFFFFF.svg?style=for-the-badge)](https://alembic.sqlalchemy.org/)
[![Google Sheets](https://img.shields.io/badge/Google%20Sheets-%23FF0000.svg?style=for-the-badge&logo=google-sheets&logoColor=FFFFFF)](https://www.google.com/sheets/)

## Установка

1. Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/fxckultimv/QRKot_spreadsheets.git
cd cat_charity_fund


2. Создать и активировать виртуальное окружение:

* Linux/macOS:

python3 -m venv venv
source venv/bin/activate


* Windows:

python3 -m venv venv
source venv/Scripts/activate


3. Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt


4. Заполнить файл .env:

touch .env


5. Применить миграции:

alembic upgrade head


## Запуск проекта

uvicorn app.main:app


## Документация

* [Redoc](http://127.0.0.1:8000/redoc)
* [Swagger](http://127.0.0.1:8000/docs)

## Автор

Комиссаров М.К.