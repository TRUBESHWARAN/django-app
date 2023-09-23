from django.db import models
from datetime import  datetime
# Create your models here.
# Class -> Table
# Attribute -> Columns

d = datetime.now()
class Enquiry(models.Model):
    name = models.CharField(max_length=30,help_text='Name should be within 30 letters')
    phone = models.BigIntegerField(help_text='Phone number should be 10 digits')
    email = models.EmailField(verbose_name='Enter Email') # verbose_name = lable name
    date = models.DateTimeField(auto_now=True)
    courses = models.CharField(max_length=50,choices=[('Java','Java'),('Python','Python3'),
                                                      ('Django','Django Framework'),('C++','C++')],default='Python')
    status = models.CharField(max_length=50,choices=[
        ('Interested','Interested'),('Not Interested','Not Interested'),("Joined","Joined"),
        ('Not Responding','Not Respondinig')],default='Interested')
# obj = ClassName()
# x = Enquiry(name='Abcd',phone=6456456546,email='abcd@gmail.com')
# x.save() --> commit the changes

# python manage.py makemigrations => collects the changes made in models.py file
# python manage.py migrate -> apply the collected changes to the database.

class Students(models.Model):
    student_id = models.CharField(max_length=15,unique=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.BigIntegerField()
    course_name = models.CharField(max_length=30,choices=[('Java','Java'),
                                                          ('Python','Python'),
                                                          ('C','C'),
                                                          ('C++','C++'),
                                                          ('Django','Django')],default='C')
    course_fee = models.IntegerField()
    address = models.TextField()
    status = models.CharField(max_length=30,choices=[('Yet to Start','Yet to Start'),
                                                     ('On Going','On Going'),
                                                     ('Hold','Hold'),
                                                     ("Discountinued",'Discontinued'),
                                                     ("Completed",'Completed')],default='Yet to Start')
