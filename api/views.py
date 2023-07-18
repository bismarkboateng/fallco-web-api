from rest_framework import generics
from .serializers import ArticleSerializer, LectureRoomSerializer
from .models import Article, LectureRoom



class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class LectureRoomListView(generics.ListAPIView):
    queryset = LectureRoom.objects.all()
    serializer_class = LectureRoomSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "id"