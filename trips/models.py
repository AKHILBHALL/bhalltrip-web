from django.db import models

# Create your models here.

class Destinations(models.Model): 
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    content = models.TextField()

   


    