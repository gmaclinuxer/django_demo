# -*- coding:utf-8 -*-
from django.contrib.auth.models import User

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     """序列化"""
#
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """创建并返回snippets实例"""
#         print 'SnippetSerializer.create'
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """更新snippet实例，并返回"""
#
#         print 'SnippetSerializer.update'
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('title', instance.code)
#         instance.linenos = validated_data.get('title', instance.linenos)
#         instance.language = validated_data.get('title', instance.language)
#         instance.style = validated_data.get('title', instance.style)
#         instance.save()
#
#         return instance

# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     # owner = serializers.CharField(source='owner.username', read_only=True)
#
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'url', 'username', 'snippets')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('id', 'url', 'highlight', 'code', 'title',
                  'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet-detail", queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'snippets')
