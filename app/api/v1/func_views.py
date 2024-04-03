from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import *

from app.models import Category, Blog
from .serializers import CategorySerializer, BlogCreateSerializer, BlogSerializer, BlogUpdateSerializer


@api_view(http_method_names=['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes([IsAuthenticated])
def create_blog(request):
    serilizer = BlogCreateSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save(author=request.user)
        return Response(serilizer.data, status=201)
    return Response(serilizer.errors, status=400)

@api_view(http_method_names=['GET'])
def blogs_list(request):
    blogs = Blog.objects.all()
    serilizer = BlogSerializer(blogs, many=True)
    return Response(serilizer.data, status=200)



@api_view(http_method_names=['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serilizer = BlogUpdateSerializer(blog, data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data, status=HTTP_201_CREATED)
    return Response(serilizer.errors, status=400)


@api_view(http_method_names=['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(status=HTTP_204_NO_CONTENT)


@api_view(http_method_names=['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=200)

















