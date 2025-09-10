from rest_framework import serializers
from .models import Question, register,login

class QuestionSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'put_date']
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ['id', 'username', 'email', 'password']
        {
            "username": "testuser",
            "email": "dias@gmail.com",
            "password": "testpassword"
        }

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = ['email','password']
