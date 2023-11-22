from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [

    path('', views.main),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('nowdate/', views.now_date),
    path('goodbye/', views.goodbye),
    path('post/', views.post_view)
]