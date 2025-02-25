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

_Или вместо пункта 2 и 3 используйте переменные окружения вашей ос_

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
   
На данном этапе у вас есть работающее приложение, соответствующее техническому заданию,  
однако база данных пока пуста.  

Чтобы ее заполнить можете перейти в админ панель [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) или [django-stripe-demo.onrender.com/admin](https://django-stripe-demo.onrender.com/admin)

**Важное замечание**  
В модели Discount поле code принимает ID купона, созданного на stripe.com. Убедитесь, что используете корректное значение.

Опубликованная демка на render.com доступна по адресу: [django-stripe-demo.onrender.com](https://django-stripe-demo.onrender.com)

Вы можете заполните базу данных через админ-панель: [django-stripe-demo.onrender.com/admin](https://django-stripe-demo.onrender.com/admin)

Поидее тредностей не должно возникнуть, но ниже я сделал описание моделей.

Логин и пароль я передал в сообщение на HH.ru


## Описание моделей


### Модель `Item`
Представляет товар, который можно приобрести.

| Поле       | Тип данных | Описание                          |
|------------|-----------|----------------------------------|
| `name`     | `CharField` | Название товара                  |
| `description` | `TextField` | Описание товара                |
| `price`    | `DecimalField` | Цена товара                     |
| `currency` | `CharField` | Валюта (например, USD, EUR)     |

---

### Модель `Discount`
Представляет скидочный купон.

| Поле     | Тип данных  | Описание                           |
|----------|------------|------------------------------------|
| `code`   | `CharField` | ID купона созданного на stripe.com |

---

### Модель `Tax`
Представляет налог.

| Поле          | Тип данных  | Описание                           |
|--------------|------------|-----------------------------------|
| `name`       | `CharField` | Название налога (например, VAT)  |
| `percentage` | `FloatField` | Процент налога                    |
| `jurisdiction` | `CharField` | Юрисдикция (например, "US")       |

---

### Модель `Order`
Представляет заказ пользователя.

| Поле        | Тип данных     | Описание                                   |
|-------------|---------------|-------------------------------------------|
| `items`     | `ManyToManyField(Item)` | Список товаров в заказе         |
| `currency`  | `CharField`     | Валюта заказа                           |
| `discount`  | `ForeignKey(Discount, null=True, blank=True)` | Примененный купон |
| `tax`       | `ForeignKey(Tax, null=True, blank=True)` | Примененный налог |

---



