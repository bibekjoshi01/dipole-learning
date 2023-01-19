from rest_framework import serializers
from django.core.exceptions import ValidationError
import re
from . validators import validate_subject_icon
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


# Core_app Serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Category
        fields = ['id', 'title']
    
    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].title()
        
        return super().update(instance, validated_data)


class SubjectListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'url']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject 
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].title()
        
        return super().update(instance, validated_data)

    def validate_icon(self, img):
        if img: 
            validate_subject_icon(img)
        return img


class UnitListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'title', 'url']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].title()
        
        return super().update(instance, validated_data)


class ChapterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'url']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'

    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].title()
        
        return super().update(instance, validated_data)


class HeadingListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heading
        fields = ['id', 'title', 'url']

class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = '__all__'

    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].title()
        
        return super().update(instance, validated_data)


class Sub_HeadingListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sub_Heading
        fields = ['id', 'title', 'url']

class Sub_HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Heading
        fields = '__all__'

    def create(self, validated_data):
        validated_data['title'] = validated_data['title'].title()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            validated_data['title'] = validated_data['title'].title()
        
        return super().update(instance, validated_data)




# Blog serializers

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title'
        ]

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['uuid','slug']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    

    def clean_body(self):
        body = self.body
        banned_words = []
        for word in banned_words:
            if re.search(r'\b' + word + r'\b', body):
                raise ValidationError('Your Comment Contains Some Malicious Worlds')

        if re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body):
            raise ValidationError("Comment Contains Links")
        
        return body 





