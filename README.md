# django_pet_project
## Интернет-магазин на Django
#### Действующий сайт расположен по ссылке:
##### https://tortiki-taganrog.ru
#### Развернут на VCD 1Gb.ru c применением технологий:
* ansible
* GitHub Actions
* gunicorn
* nginx
* certbot
* docker-compose
* smtp
* rsync
* ssh
#### Проект является интеренет-магазином,   предоставляющим кондитерские изделия на заказ.
#### Использовалось в проекте:
```bash
  * Frontend - Bootstrap 5
  * Backend - Django 4.2
  * DataBases - Postgresql 15
```
## Описание проекта.

*  В данном e-comerce решении используются 9 приложений:
```bash
  - "shop" - раздел (функционал) самого  магазина с категориями и товарами.  
  - "cart" - корзина для покупок товара.
  - "orders" - оформление заказов, запись их в БД.
  - "users" - регистрация и авторизация пользователе(возможность востановить пароль или изменить наомер ntktajyf)
  - "cupons" - применение скидок и акций
  - "foto_gallery" - добавление фотографий на сайт с сохранением в БД
  - "contact_form" - заказа обратного звонка с записью в БД
  - "feedback" - форма обратной связи с БД и почтовой рассылкой 
  - "payment" - приложение электронной оплаты картой или яндекс деньгами в данном случае настроина но отключенна
 ``` 
Через админ панель можно:
  - Добавлять, удалять товары и категории а так же 
описание к ним.
  - Просматривать и отмечать заказы.
  - Добавлять и удалять купоны на скидки.
  - Просматривать пользователей и их профили.
  - Просматривать базу контаков и сообщений обратной связи пользователей,
  - Наполнять фотогалерею.
  - Вывести заказы в CSV файл.

Пользователи могут:
  - Выбирать категории товаров,
  - Выбирать товары, 
  - Добавлять в корзину, 
  - Применять купоны на скидки, 
  - Оформлять заказы,
  - Просматривать фотогалерею,
  - Заполнять формы обратной связи. 

После оформления заказа присылается сообщение по электронной почте, с деталями заказа а так же PDF файл. 

Реализованна регистрация и 
авторизация пользователей.

Профиль пользователя с возможностью просмотра заказов.

В форме обратной связи пользователь может отправить свое сообщение

## Документация по проекту.

### Для запуска проекта необходимо:

* Создать и перейти в директорию, которую будет скопирован проект.
```bash
mkdir django-project
cd django-project
```

* Настроить виртуальное окружение 
```bash
python -m venv env
python . ./env/bin/activate
#source ./env/bin/activate .
```
* Скопировать репозиторий себе на локальный компьютер
```bash
git clone https://github.com/kolesnikovvitaliy/django-pet-project.git
```
* Перейти в директорию django-pet-project
```bash
cd django-pet-project
```

* Установить зависимости:
```bash
pip install -r requirements.txt
```
* Перейти в директорию приложения django_pet_project
```bash
cd django_pet_project
```
### Выполнить следующие команды:

* Команда создания миграций приложения для базы данных
```bash
python manage.py migrate --noinput
```
* Команда для регистрации статистических файлов приложения 
```bash
python manage.py makemigrations --noinput
python manage.py collectstatic
```
* Команда для регистрации суперпользователя базы данных - "admin". Можете заменить на желаемое.
```bash
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '','admin' )" | python manage.py shell
```
* Команда для запуска приложения:
```bash
python manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python manage.py makemigrations
python manage.py migrate
```
> Используйте адрес: http://localhost:8000/

## Запуск приложения с помощью docker-compose
#### 
* Создать и перейти в директорию, которую будет скопирован проект.
```bash
mkdir django-project
cd django-project
```
* Скопировать репозиторий себе на локальный компьютер
```bash
git clone https://github.com/kolesnikovvitaliy/django-pet-project.git
```
* Перейти в директорию django-pet-project
```bash
cd django-pet-project
```
* Перейти в директорию django_pet_project/django_pet_project
```bash
cd django_pet_project
cd django_pet_project
```
* Раскомментировать в файле settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_db',
        'USER': 'postgres',
        'PASSWORD': 1234,
        'PORT' : 5432,
        'HOST': 'db',
        'ATOMIC_REQUESTS': True,
    },
}
```
* И закомментировать 
```python
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
```
* Вернуться в директорию django-pet-project
```python
cd ../../
```
* Запустить приложение с применением docker-compose
```bash
docker-compose up 
```
> Используйте адрес: http://localhost:8000/
# Для разворачивания на сервер вам потребуется:
* Учетная запись на Docker Hub,
* Установленный на сервере docker и docker-compose,
* Установленный на вашем локальном компьютере Ansible,
* Соединение с сервером по SSH с помощью приватного ключа.
  
### Если все это имеется, тогда требуется выполнить, на своем локальном компьютере, следующие команды:
* Создать и перейти в директорию, которую будет скопирован проект.
```bash
mkdir django-project
cd django-project
```
* Скопировать репозиторий себе на локальный компьютер
```bash
git clone https://github.com/kolesnikovvitaliy/django-pet-project.git
```
* Перейти в директорию django-pet-project
```bash
cd django-pet-project
```
* Отредактировать файл .env 
```bash
vim .env
```  
```bash
REGISTRY = 'УКАЗАТЬ ВАШ ЛОГИГ ОТ Docker Hub'
IMAGE_TAG = 'Номер версии контейнера' 
HOST = 'IP вашего сервера на который планируете разворачивать сайт в формате 0.0.0.0 '
PORT = 'Порт по которому происходит соединение ssh, по умолчанию "22"'
```  
* Далее установите Ansible на свой компьютер
```bash
sudo apt update
sudo apt install ansible
```  
### Выполните команду для автоматизированного разворачивания сайта на ваш сервер:
```bash
make init
```  
> Используйте адрес: http://localhost:8000/
#### Если вы хотите:
* Остановить показ сайта:
```bash
make stop
```  
* Снова запустить показ сайта:
```bash
make start
``` 
* Откатить сайт к предидущей версии:
```bash
make rollback
``` 