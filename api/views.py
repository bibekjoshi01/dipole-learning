from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from blog.models import (
    Post, 
    Tag, 
    Category, 
    Comment,
)

from core_app.models import (
    Category,
    Subject,
    Unit,
    Chapter,
    Heading,
    Sub_Heading,
)

from . serializers import (
    #blog serailizers
    TagSerializer,
    CategorySerializer,
    PostSerializer,
    CommentSerializer,

    # core_app serializers
    ChapterSerializer,
    SubjectListSerializer,
    SubjectSerializer,
    UnitListSerializer,
    UnitSerializer,
    ChapterListSerializer,
    ChapterSerializer,
    HeadingListSerializer,
    HeadingSerializer,
    Sub_HeadingListSerializer,
    Sub_HeadingSerializer,
)


class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class SubjectViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Subject.objects.all()
    
    def get_serializer_class(self):
        serializer_class = SubjectListSerializer
        if self.request.method == 'GET':
            if self.action == 'list':
                serializer_class = SubjectListSerializer
            else: 
                serializer_class = SubjectSerializer
        else: 
            serializer_class = SubjectSerializer
        
        return serializer_class
        

class UnitViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Unit.objects.all()

    def get_serializer_class(self):
        serializer_class = UnitListSerializer
        if self.request.method == 'GET':
            if self.action == 'list':
                serializer_class = UnitListSerializer
            else: 
                serializer_class = UnitSerializer
        else: 
            serializer_class = UnitSerializer
        
        return serializer_class

class ChapterViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Chapter.objects.all()

    def get_serializer_class(self):
        serializer_class = ChapterListSerializer
        if self.request.method == 'GET':
            if self.action == 'list':
                serializer_class = ChapterListSerializer
            else: 
                serializer_class = ChapterSerializer
        else: 
            serializer_class = ChapterSerializer
        
        return serializer_class

class HeadingViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Heading.objects.all()

    def get_serializer_class(self):
        serializer_class = HeadingListSerializer
        if self.request.method == 'GET':
            if self.action == 'list':
                serializer_class = HeadingListSerializer
            else: 
                serializer_class = HeadingSerializer
        else: 
            serializer_class = HeadingSerializer
        
        return serializer_class

class Sub_HeadingViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Sub_Heading.objects.all()

    def get_serializer_class(self):
        serializer_class = Sub_HeadingListSerializer
        if self.request.method == 'GET':
            if self.action == 'list':
                serializer_class = Sub_HeadingListSerializer
            else: 
                serializer_class = Sub_HeadingSerializer
        else: 
            serializer_class = Sub_HeadingSerializer
        
        return serializer_class



# Blog Viewsets 

class TagViewset(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

