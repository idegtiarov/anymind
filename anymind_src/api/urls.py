from django.urls import path

from api.views import hashtag, users

urls_list = [
    path('hashtag/<str:tag>', hashtag),
    path('users/<str:user>', users)
]

urlpatterns = (urls_list, 'api')
