from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.LoginApiView.as_view()),
    path('registration/', views.RegisterApiView.as_view()),

]
