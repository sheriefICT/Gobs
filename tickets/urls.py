from django.urls import path
from .views import *

urlpatterns = [
    #1
    # path("django/no_rest_from_model/", no_rest_from_model_query),

    #2  GET POST from 
    path("rest/fbv/", rest_for_function_based_views_List),
    #3 ['GET', 'POST', 'DELETE']
    path("rest/fbv/<int:pk>", rest_for_function_based_views_List_as_pk),



   
]