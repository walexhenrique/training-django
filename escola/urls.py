from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api/v1/student', views.StudentViewSet, basename='student')
app_name = 'escola'


urlpatterns = [
    # path('api/v1/student/', views.StudentViewSet.as_view({'get':'list', 'post': 'jumento'}), name='student-list'),
    # path('api/v1/student/<int:pk>/', views.StudentViewSet.as_view({'get':'retrieve'}), name='student-detail'),
]
urlpatterns += router.urls


print(router.urls)
