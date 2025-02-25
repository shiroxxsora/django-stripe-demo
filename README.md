## **Запуск проекта**

1. Создайте виртуальное окружение:

    ```bash
    python -m venv .venv
    ```

2. Создайте файл `.env` в каталоге `stripe_demo/`.

3. Добавьте в файл `.env` следующие переменные:

    ```plaintext
    SECRET_KEY = "ваш-секретный-ключ"
    STRIPE_SECRET_KEY = "ваш stripe sk"
    STRIPE_PUBLIC_KEY = "ваш stripe pk"
    ```

4. Активируйте виртуальное окружение:

    - Для Windows:
      ```bash
      .venv\Scripts\activate.ps1
      ```
    - Для Linux:
      ```bash
      source .venv/bin/activate
      ```

5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

6. Создание суперпользователя:

    ```bash
    python stripe_demo/manage.py createsuperuser
    ```

7. Создайте миграции:

    ```bash
    python stripe_demo/manage.py makemigrations
    ```

8. Примените миграции:

    ```bash
    python stripe_demo/manage.py migrate
    ```

9. Запустите сервер:

    ```bash
    python stripe_demo/manage.py runserver
    ```
   
На данном этапе у вас уже будет настроенное приложение. Заполните базу данных через админ-панель.

Опубликованная демка на render.com доступна по адресу: [django-stripe-demo.onrender.com](https://django-stripe-demo.onrender.com)