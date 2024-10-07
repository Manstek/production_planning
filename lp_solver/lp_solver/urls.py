from django.contrib import admin
from django.urls import path
from solver.views import solve_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', solve_view, name='solve'),
]
