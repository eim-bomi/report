from django.urls import re_path, include

urlpatterns = [
    re_path(r'^portfolio/', include('portfolio.urls')),
]