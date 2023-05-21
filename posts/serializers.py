from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import Post,Comment

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',
        ]
        # exclude = ['content',]
        depth = 1

class PostRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',
        ]
        # exclude = ['content',]
        depth = 1

class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
        ]

class PostDeleteModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'content',
        ]

