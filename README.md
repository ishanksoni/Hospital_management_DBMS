# Hospital_management_DBMS
Dbms course Project Under Prof. Antriksh Goswami  
This is fully functioning website for a clinic or small scale hospitals to manage patients and their records  

Step to install and Run:  

Necessory Pre-Installaions  
1.PYTHON veriosn 3  
2.MYSQL workbench or something for DATABASE  
3. pip(python installation pakage)  
4. Django version 3  
  
Run following command in cmd   
pip3/pip install mysqlclient  
  
Create a database in mysql named " myHospital"  
Import database mysql file  
Move to project directroy and run following command  
1. Python manage.py makemigrations  
2. Python manage.py migrate  
(this will create or link all database tables to project)  

Make a environmental varible file and export follwing data  
a. your or company email address and password  
b. security key  
  
Then reload the project and run following command  
1. python manage.py make runserver   
  
and open the local host port and enjoy!!!  
