from django.urls import path
from .views import ArticleListCreateView, LectureRoomListView, ArticleDetailView


urlpatterns = [
    path("articles/", ArticleListCreateView.as_view(), name="list articles"),
    path("articles/<int:id>/", ArticleDetailView.as_view(), name="articl detail"),
    path("lecture-rooms/", LectureRoomListView.as_view(), name="lecture rooms")
]
