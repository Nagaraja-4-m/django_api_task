from django.db import models

# Create your models here.

class Userr(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    mobile_number=models.IntegerField()
    email=models.EmailField()
    user_id=models.CharField(max_length=20)
    password=models.CharField(max_length=16)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name