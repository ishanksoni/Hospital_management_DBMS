import os
import smtplib

recepent = "201851051@iiitvadodara.ac.in"
email = os.environ.get('EMAIL')
email_pass = os.environ.get('EMAIL_PASS')


un  = 'test'

def send(un,recepent,dob):


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email,email_pass)
        sub = "Succesful Registration"
        body = "This is to inform you that your registration is successful in myHospital \n\n your user_id is "+un+" And Password is:"+dob+" \n Happy Good day!"
        msg = f'Subject: {sub} \n\n{body}'
        smtp.sendmail(email,recepent,msg)
