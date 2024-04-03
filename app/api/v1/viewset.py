from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app.api.v1.serializers import BlogSerializer, CommentCreateSerializer
from app.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    @action(detail=True, methods=['post'])
    def comment_create(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        data = request.data
        serializer = CommentCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user, blog=blog)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























