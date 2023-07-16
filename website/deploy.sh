bash
python -m virtualenv venv
source venv/bin/activate
python -m pip install Django
git pull [https://bmstu.codes/b.edaev/djangoproject]
cd website/website
nano settings.py

# *****
# Дальше добавляем 'dc-webdev.bmstu.ru' в ALLOWED_HOSTS в настройках Джанго-приложения
# ******
cd ..
nohup python manage.py runserver 0.0.0.0:8123

# Порт 8001 заменить на закрепленный в таблице