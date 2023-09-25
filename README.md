# **Приложение Загрузки и обработк файлов** 
#### проект доступен по [адресу](http://158.160.14.244/)
---

### Описание

Проект предоставляет пользователям следующие возможности:
  - Загружать файлы через админ-панель

---

#### Установка Docker

## Windows

[Скачать можно тут на официальном сайте](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module&_gl=1*1bsd02s*_ga*NzI3MDYzNDguMTY5MzM5MTEwNQ..*_ga_XJWPQMJYHQ*MTY5MzM5MTEwNC4xLjEuMTY5MzM5MTE0NS4xOS4wLjA.)

## Ubuntu

Для начала необходимо скачать и выполнить официальный скрипт:
```bash
apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

При необходимости удалить старые версии Docker:
```bash
apt remove docker docker-engine docker.io containerd runc 
```

Установить пакеты для работы через протокол https:
```bash
apt update
```
```bash
apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y 
```

Добавить ключ GPG для подтверждения подлинности в процессе установки:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Добавить репозиторий Docker в пакеты apt и обновить индекс пакетов:
```bash
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
```
```bash
apt update
```

Установить Docker(CE) и Docker Compose:
```bash
apt install docker-ce docker-compose -y
```

Проверить что  Docker работает можно командой:
```bash
systemctl status docker
```

Подробнее об установке можно узнать по [ссылке](https://docs.docker.com/engine/install/ubuntu/).

---
### База данных и переменные окружения

Проект использует базу данных PostgreSQL.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в папке "./infra/".

Шаблон для заполнения файла ".env":
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY='Здесь указать секретный ключ'
ALLOWED_HOSTS='Здесь указать имя или IP хоста' (Для локального запуска - 127.0.0.1)
```

---
### Команды для запуска

Перед запуском необходимо склонировать проект:
```bash
HTTPS: git clone https://github.com/Svyat94/api_upload_files.git
SSH: git clone git@github.com:github.com/Svyat94/api_upload_files.git
```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
Cоздавать и запустить контейнеры.  
Из папки "./nginx/" выполнить команду:
```bash
docker-compose up -d
```

После успешного запуска контейнеров выполнить миграции:
```bash
docker-compose exec backend python manage.py migrate
```

Создать суперюзера (Администратора):
```bash
docker-compose exec backend python manage.py createsuperuser
```

Собрать статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```

Теперь доступность проекта можно проверить по адресу [http://127.0.0.1/](http://127.0.0.1/)

---
#### Техническая информация

Стек технологий: Python 3, Django, DRF, Docker, PostgreSQL, nginx, gunicorn

---
#### Автор

[Svyatoslav](https://github.com/svyat94)
