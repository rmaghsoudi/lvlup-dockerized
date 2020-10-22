from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('entries/', views.EntryDetail.as_view()),
    path('entries/<int:pk>', views.EntryDetail.as_view()),
    path('users/', views.UserDetail.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    # path('api/public', views.public),
    # path('api/private', views.private),
    # path('api/private-scoped', views.private_scoped),
]

urlpatterns = format_suffix_patterns(urlpatterns)
