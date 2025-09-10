from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .serializers import QuestionSerilalizer,RegisterSerializer,LoginSerializer
from .models import Question, register,login
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication

@api_view(['GET'])
@authentication_classes([TokenAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def api(request):
    questions = Question.objects.all()
    serializer = QuestionSerilalizer(questions, many=True)
    return Response(serializer.data,status=status.HTTP_418_IM_A_TEAPOT)

# @api_view(['POST'])
# def api_index(request):
#  serialize = QuestionSerilalizer(data=request.data)
#  if serialize.is_valid():
#      question = serialize.save()
#      return Response(serialize.data,status=status.HTTP_201_CREATED)
#  else: 
#     return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
 
# { "question_text": "What is the capital of France?", "put_date": "2023-10-01T12:00:00Z"}


# @api_view(['GET','PUT','DELETE'])
# def api_question_detail(request,pk):
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return Response({"error": "Question not found"},status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#        serialier = QuestionSerilalizer(question)
#        return Response(serialier.data)
    
#     elif request.method == 'PUT':
#        serialier = QuestionSerilalizer(question, data=request.data)
#        if serialier.is_valid():
#           serialier.save()
#           return Response(serialier.data)
#        return Response(serialier.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#        question.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
    

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerilalizer

class Questiondetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerilalizer

@api_view(['POST'])
def register(request):
    if request.method == 'GET':
        return Response({'message': 'Please use POST to register'})
    
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        return Response(request.data)
    
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        