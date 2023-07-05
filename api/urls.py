from django.urls import path
from .views import ArticleListCreateView, LectureRoomListView


urlpatterns = [
    path("articles/", ArticleListCreateView.as_view(), name="list articles"),
    path("lecture-rooms/", LectureRoomListView.as_view(), name="lecture rooms")
]
