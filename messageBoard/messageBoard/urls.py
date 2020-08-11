
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    re_path('static/(?P<path>.*)', serve,
        {'document_root': settings.STATIC_ROOT}, name='static')
]

# 设置404、500错误状态码
from index import views
handler404 = views.page_not_found
handler500 = views.page_error