from django.urls import path

from .views import (
    EmployeeCreateAPIView,
    EmployeeDeleteAPIView,
    EmployeeDetailAPIView,
    EmployeeListAPIView,
    EmployeeUpdateAPIView,
)


urlpatterns = [

    path(
        '',
        EmployeeListAPIView.as_view(),
        name='employee-list'
    ),

    path(
        'create/',
        EmployeeCreateAPIView.as_view(),
        name='employee-create'
    ),

    path(
        '<int:pk>/',
        EmployeeDetailAPIView.as_view(),
        name='employee-detail'
    ),

    path(
        '<int:pk>/update/',
        EmployeeUpdateAPIView.as_view(),
        name='employee-update'
    ),

    path(
        '<int:pk>/delete/',
        EmployeeDeleteAPIView.as_view(),
        name='employee-delete'
    ),
]