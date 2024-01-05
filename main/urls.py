from django.urls import path
from .views import *

urlpatterns=[
    path('service',service_read),
    path('create_service',create_service),
    path('update_service',update_service),
    path('delete_service',delete_service),
    path('create_mashgulot',create_mashgulot),
    path('update_mashgulot',update_mashgulot),
    path('delete_mashgulot',delete_mashgulot)
]