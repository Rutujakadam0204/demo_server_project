from django.db import models

# Create your models here.
# Create your models here.
# class Core1_Model(models.Model):
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     upload = models.FileField()

class Core1_Model2(models.Model):
    name = models.CharField(max_length=10)
    uploaded_at = models.DateTimeField()

    class Meta:
        abstract = True
    # upload = models.FileField()

class Core1_Model3(Core1_Model2):
    sent = models.CharField(max_length=10)

class Document(Core1_Model2):
    type = models.CharField(max_length=100)

class Widget(models.Model):
    name = models.CharField(max_length=140)