from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author_of_publication', 'publishing_house', 'date_of_publication', 'ISSN', 'DOE', 'content')