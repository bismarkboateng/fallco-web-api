from django.db import models
from django.contrib.auth.models import User


class Rep(models.Model):
    name = models.CharField(max_length=200)
    RepId = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Rep"

    def __str__(self):
        return f"{self.name}"
    



class Article(models.Model):
    title = models.CharField(max_length=700)
    content = models.TextField()
    article_image = models.ImageField(default="images")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title[:10]}"
    



class LectureRoom(models.Model):
    class_room = models.CharField(max_length=10)
    class_size = models.IntegerField()
    building_name = models.CharField(max_length=600)
    is_available = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "LectureRoom"

    def __str__(self):
        return f"{self.class_room} - {self.class_size}"