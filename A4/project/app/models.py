from django.db import models

GENDER_CHOICES = [
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Other'),
]

class StudentsInfo(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15) 

    def __str__(self):
        return self.name
