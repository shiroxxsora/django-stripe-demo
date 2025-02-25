## **Запуск проекта**

1. Создать виртуальное окружение `python -m venv .venv`
2. Создать файл `.env` в каталоге `stripe_demo/`
3. Добавить в файл `.env` переменную `SECRET_KEY = "ваш-секретный-ключ"`
4. Активировать окружение `.venv/Scripts/activate.ps1` (windows) `source .venv/bin/activate` (linux)
5. Устанавить зависимости `pip install -r requirements.txt` 
6. Запуск сервера `python stripe_demo/manage.py runserver`