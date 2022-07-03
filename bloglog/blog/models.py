from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=250)

class Log(models.Model):
    LOG_TYPE_TEXT = 'text'

    LOG_TYPES = (
        (LOG_TYPE_TEXT, "Text"),
    )

    log_type = models.CharField(max_length=250, choices=LOG_TYPES)
    text = models.CharField(max_length=250)
    posts = models.ManyToManyField(Post)
    
