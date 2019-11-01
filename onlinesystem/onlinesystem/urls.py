from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.returnToHomeView.as_view()),
    path('booksystem/', include('booksystem.urls')),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
]
