from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import IndexPage, PostsListView, PostsDetailView, PostViewset

urlpatterns = [
    path('', IndexPage.as_view()),
    path('posts/', PostsListView.as_view()),
    path('posts/<slug:slug>', PostsDetailView.as_view(), name='post-detail'),
]

router = DefaultRouter()
router.register(r'post-api', PostViewset, )
urlpatterns += router.urls
