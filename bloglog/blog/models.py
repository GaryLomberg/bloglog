from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Log(BaseModel):
    LOG_TYPE_TEXT = 'text'

    LOG_TYPES = (
        (LOG_TYPE_TEXT, "Text"),
    )

    log_type = models.CharField(max_length=250, choices=LOG_TYPES)
    text = models.CharField(max_length=250)
    posts = models.ManyToManyField(Post)
    
    def __str__(self):
        return f"{self.log_type.title()} Log {self.pk}"
