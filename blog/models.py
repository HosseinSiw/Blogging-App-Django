from django.db import models
from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True,)
    image = models.ImageField(upload_to=MEDIA_ROOT + "blog", blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def add_like(self):
        self.likes += 1
