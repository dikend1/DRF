from django.urls import path
from .views import api,QuestionList,Questiondetail,register,login
app_name = 'clone'
urlpatterns = [
    path('api/', api, name='api'),
    # path('api/post/', api_index, name='api_post'),
    # path('api/questions/<int:pk>/',api_question_detail,name='def api_question_detail:'),
    path('api/register/',register,name='register'),
    path('api/login/',login,name='login'),


    # generics
    path('api/questions/',QuestionList.as_view(),name='question_post:'),
    path('api/questions/<int:pk>/',Questiondetail.as_view(),name='question_detail:')

]
