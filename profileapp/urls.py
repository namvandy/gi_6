from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns=[
    path('create/', ProfileCreateView.as_view(), name='create'),
    #수정하는 것이므로 key를 넘겨받아야함
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),

]