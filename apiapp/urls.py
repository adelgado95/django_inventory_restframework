from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiapp import views

urlpatterns = [
    path('producto/<int:pk>/', views.ProductoDetail.as_view()),
    path('productos/',views.ProductoListApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)