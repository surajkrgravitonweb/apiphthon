from django.db import models

# Create your models here.


# create company models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('NON-IT','NON-IT'),
                                                  ('MOBILE','MOBILE')
                                                  ))
    add_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    

def __str__(self):
    return self.name

# employee model 

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.IntegerField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,
                              choices=(('Manage','Manage'),
                                                     ('Frontend Developer',
                                                      'Frontend Developer'),
                                                      ('Project Lead','Project Lead'),
                                                      ('Full stack developer','Full stack Developer')))

    company=models.ForeignKey(Company, on_delete=models.CASCADE)                                                 
    