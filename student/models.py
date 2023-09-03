from django.db import models

# Create your models here.
class PersonInfoCreate(models.Model):
    SECTION_LIST = (
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        ('S8', 'S8'),
    )
    userid = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    section = models.CharField(max_length=20, choices=SECTION_LIST,default='Default Value')

class Subjects(models.Model):
    SUBJECT_LIST = (
        ('Sub1', 'Subject1'),
        ('Sub2', 'Subject2'),
        ('Sub3', 'Subject3'),
        ('Sub4', 'Subject4'),
        ('Sub5', 'Subject5'),
        ('Sub6', 'Subject6'),
    )
    person = models.ForeignKey(PersonInfoCreate, on_delete=models.CASCADE, null=True)
    sub = models.CharField(max_length=20, choices=SUBJECT_LIST)


class Results(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    result = models.CharField(max_length=3,default='',null=True)