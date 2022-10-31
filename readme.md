# Тестовое задание
Выполнил <strong>Кожинов Виталий</strong>

<a href="https://docs.yandex.ru/docs/view?url=ya-mail%3A%2F%2F180988410024962362%2F1.2&name=main.pdf&uid=635589445">Файл с заданием</a>

### Запуск проекта через Docker


1. Создать тестовые значения для БД(slite3) и внести фикстуры

        docker-compose run filldb

2. запустить сервер и 

        docker-compose up web

3. Перейти по адресу:

        http://localhost:8000

### Запуск без Docker

1. Скачать репозиторий.

        git clone https://github.com/LosSantosWhite/spacecorp.git

2. Перейти в папку проекта.

        cd spacecorp/

2. Создать виртуальное окружение.

        python3 -m venv venv

3. Установить зависимости.

        pip install -r requirements.txt

4. Создать базу данных и наполнить таблицу тестовыми значениями

        python manage.py migrate

        python manage.py loaddata fixtures.json

5. Запустить локальный сервер

        python manage.py runserver

6. Перейти по адресу

        http://localhost:8000


### Запуск тестов

    docker-compose run test


#### Супер пользователь
Login

    admin

Password

    admin



