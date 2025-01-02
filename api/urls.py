from django.urls import path
from .views import MainApiView, ProductModelView

urlpatterns = [
    path('', MainApiView.as_view()),
    path('products/', ProductModelView.as_view())
]