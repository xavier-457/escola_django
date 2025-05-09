from django.contrib import admin
from django.urls import path, include  # 👈 não esqueça o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),  # 👈 linka o app cadastro
]

