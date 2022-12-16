from django.urls import path
from main import views

urlpatterns = [
    path('products/', views.ItemApiView.as_view()),
    path('create_item/', views.CreateItemView.as_view()),

]
