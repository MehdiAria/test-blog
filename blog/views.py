from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from blog.models import Post
from blog.serializers import PostSerializer


class IndexPage(TemplateView):
    template_name = 'home_page.html'


# class IndexPage(TemplateView):
#     template_name = 'home_page.html'

class PostsListView(ListView):
    template_name = 'posts.html'
    queryset = Post.objects.all()


class PostsDetailView(DetailView):
    template_name = 'post.html'

    def get_object(self, queryset=None):
        post_slug = self.kwargs.get('slug')
        try:
            post = Post.objects.get(slug=post_slug)
        except:
            raise Http404('Post Not Found!!!!')
        return post


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
