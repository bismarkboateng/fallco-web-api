from . import models
from rest_framework.serializers import ModelSerializer 


class RepSerializer(ModelSerializer):
    class Meta:
        model = models.Rep
        fields = ["name"]


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ["title", "content", "article_image", "created_at"]


class LectureRoomSerializer(ModelSerializer):
    class Meta:
        model = models.LectureRoom
        fields = "__all__"