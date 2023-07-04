from django.db import models

# Create your models here.
class Rep(models.Model):
    name = models.CharField(max_length=200)
    RepId = models.IntegerField()

    def __str__(self):
        return f"{self.name}"




class Article(models.Model):
    title = models.CharField(max_length=700)
    content = models.TextField()
    # add an image field here after installing pillow
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title[:10]}"
    



class LectureRoom(models.Model):
    class_room = models.CharField(max_length=10)
    class_size = models.IntegerField()
    building_name = models.CharField(max_length=600)
    is_available = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.class_room} - {self.class_size}"