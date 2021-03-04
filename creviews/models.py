from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class App(models.Model):
    app_ID = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Review(models.Model):
    review_ID = models.CharField(max_length=50, primary_key=True)
    content = models.CharField(max_length=1000)
    date = models.DateField()
    rating = models.IntegerField()
    app = models.ForeignKey('App', on_delete=models.CASCADE)
    reviewer_username = models.CharField(max_length=50)


class Reply(models.Model):
    reply_content = models.CharField(max_length=1000)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    date = models.DateField()


class Report(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    result = models.CharField(max_length=50)
    date = models.DateField()
