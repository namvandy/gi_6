from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'
urlpatterns = [


    path('create/', AccountCreateView.as_view(), name='create'), #회원가입

    path('login/',
         LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),
    #로그인

    path('logout/',
         LogoutView.as_view(),
         name='logout'), #<int:pk>어떤 것을 가져올지 인자 지정하는 것
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]