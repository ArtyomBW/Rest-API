from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from apps.models import Category, Book

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',

class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = 'id', 'title', 'price', 'description',

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'email', 'first_name', 'last_name', 'password'

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        return User.objects.create(**validated_data)





