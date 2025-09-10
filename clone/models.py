from django.db import models

class register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email 

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    put_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text   
