from rest_framework import serializers
from .models import Subject,Preprint,Author,Tag


# Serializers

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class PreprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preprint
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
