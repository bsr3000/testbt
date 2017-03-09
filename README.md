# testbt
test project for bt pol

REST Api mostly ready, it does create, retrieve, update, delete functions on each model.

Android application partially done, didn`t implement all what I wanted, because of time

Dashboard, implemented a little dashboard, to manage data, didn`t implement all what I wanted, because of time

urls:
/admin/ - Admin interface(Django generated)
/core/api/ - REST Api
/dashboard/ - Dashboard

login credentials:
login - testerbt
password - lkjhgfdsa647484

JS and CSS files generated

Server setup:

Create - virtualenv env

source env/bin/activate

1. pip install -r requirments.txt

2. settings.py

2.1 DB == PSQL

2.2 DATABASES {
#Change this data to your create DB
        'NAME': 'testbt',
        'USER': 'testbtuser',
        'PASSWORD': 'testbt',
        'HOST': '127.0.0.1',
        'PORT': '5432',
}

2.3 ./manage.py migrate

3. ./manage.py loaddata ./data.json

if static won`t show, ./manage.py collectstatic

4. Start server - ./manage.py runserver host:port

5. login url host:port/admin/