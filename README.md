# Clinic Management 

DBMS(CS204) project under Prof. Antriksh Goswami, made by [@ishanksoni](https://github.com/ishanksoni) and [@HrithikVaishnav](https://github.com/HrithikVaishnav)

## Development 🔧   
<img src="https://img.icons8.com/color/96/000000/django.png"/>   &nbsp;    <img src="https://img.icons8.com/ios/96/000000/mysql-logo.png"/>
## Setup
>>Clone repository  
Set up  virtual environment  
Move to project directory


### Start
Install pakages using [pip](https://pip.pypa.io/en/stable/)


```sh
$ pip install -r requirements.txt
```
## Setup Following environmental variable 
```
DB_USER="<db_user>"
DB_PASS="<db_pass>"
EMAIL="<company_mail_address>"
EMAIL_PASS="<mail_password>"
```
>>Create database in mysql named "myHospital" 

## Run proj. by following command

```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### Authors :pencil:
[Ishank Soni](https://github.com/ishanksoni) and [Hrithik Vaishnav](https://github.com/HrithikVaishnav)
