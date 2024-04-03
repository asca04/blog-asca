from django.urls import path

from .func_views import create_blog, update_blog, create_category, blogs_list, categories_list
from .viewset import BlogViewSet
from .generic_views import CategoryCreateAPIView, CategoryListAPIView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blogs', BlogViewSet, basename='blogs')

#                Function-Views

urlpatterns = [
    path('blog-create/', create_blog, name='blog-create'),
    path('blog-update/<int:pk>/', update_blog, name='blog-update'),
    path('category-create/', create_category, name='category-create'),
    path('categories/', categories_list, name='categories-list'),
    path('blog-list/', blogs_list, name='blog-list')

]

#                Generic-Views

# urlpatterns = [
#     path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
#     path('categories-list/', CategoryListAPIView.as_view(), name='categories-list')
# ]

urlpatterns += router.urls
