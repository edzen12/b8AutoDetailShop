## Наш второй сайт - интернет магазин с Backend 8

### Инструкции по установке:
### скачиваем этот проект через команду 
#### git clone https://github.com/edzen12/b8AutoDetailShop.git
### открываем в VSCode эту папку и после открываем терминал

### и пишем команды если Windows
#### python -m venv venv
#### .\venv\Scripts\activate
#### pip install -r requirements.txt
#### python manage.py migrate
#### python manage.py createsuperuser
#### python manage.py runserver

### и пишем команды если MacOS/Linux
#### python3 -m venv venv
#### source venv/bin/activate
#### pip install -r requirements.txt
#### python manage.py migrate
#### python manage.py createsuperuser
#### python manage.py runserver