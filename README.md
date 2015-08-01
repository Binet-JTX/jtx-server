# jtx-django
## API service for JTX website

### Installation

Adapt `jtx/settings/dev_local.py` to your local MySQL settings.

Python3 is required. pip is highly recommanded !

Run the following commands in a shell :
```
pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py runserver
```
