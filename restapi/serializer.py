from rest_framework import serializers
from .models import Article

# =========================Using Serializer=========================================

# class ArticleSerializer(serializers.Serializer):
#     author = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=100)
#     date = serializers.DateTimeField()
#     email = serializers.EmailField(max_length=100)

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.date = validated_data.get('date', instance.date)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance


# ===========================Model serializer==============================================


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
