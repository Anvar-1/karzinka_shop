from django.urls import path
from .views import MainApiView, ProductModelView, MainView

urlpatterns = [
    path('', MainApiView.as_view()),
    path('products/', ProductModelView.as_view()),
    path('products/<int:pk>/', MainView.as_view())
]