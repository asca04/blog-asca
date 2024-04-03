from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.v1.serializers import CategorySerializer, BlogSerializer
from app.models import Category, Blog
from app.permissions import IsOwner


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class BlogUpdateAPIView(APIView):
    permission_classes = [IsOwner]
    authentication_classes = (TokenAuthentication,)



    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        self.check_object_permissions(request, blog)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class BlogDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Blog.objects.all()



















