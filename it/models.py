from django.db import models

class NewUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_number = models.CharField(max_length=30)
    second_number = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    inlineRadioOptions = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    classe = models.CharField(max_length=30)
    info_sup = models.CharField(max_length=30)
    
