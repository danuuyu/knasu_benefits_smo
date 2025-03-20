## 🚀 Установка и запуск

1. Клонируйте репозиторий на ваш компьютер:
   ```bash
   git clone https://github.com/danuuyu/knastu_algorithms.git

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate.bat  # Windows

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Создайте файл .env в корневой директории проекта и добавьте в него следующие переменные:
   ```bash
   TOKEN=<ваш_токен>
   ADMIN_ID=<ваш_айди>
   HOST=0.0.0.0  # Пример
   PORT=8000  # Пример
   BASE_URL=https://danuuyu.loca.lt  # Пример, замените на ваш URL

>  - TOKEN: Токен вашего бота, полученный от [BotFather](t.me/BotFather "Тык").
>  - ADMIN_ID: Ваш ID в Telegram (можно узнать у бота [@getmyid_bot](t.me/getmyid_bot "Тык").
>  - HOST и PORT: Адрес и порт, на котором будет запущен сервер.
>  - BASE_URL: Внешний URL вашего сервера. Вы можете использовать [localtunnel](https://localtunnel.github.io/www/ "Тык") для получения временного URL.

5. Установите localtunnel глобально (если еще не установлен) через Терминал:
> Для работы localtunnel требуется NodeJS.
   ```bash
   npm install -g localtunnel
   ```
   Запустите localtunnel на указанном порту (например, 8000):
   ```bash
   lt --port 8000
   ```
   Скопируйте предоставленный URL (например, https://danuuyu.loca.lt) и вставьте его в переменную BASE_URL в файле .env.

6. Перейдите по предоставленному URL и введите Tunnel Pssword (пароль берется из https://loca.lt/mytunnelpassword). 

7. Запустите стартовый файл (aiogram_run.py):
