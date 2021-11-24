from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.read_calc, name='home'),
    path('fish/', views.fish_search_view),
    path('fish/<int:id>/', views.fish_search_view),
    #path('admin/', admin.site.urls)
    #path('calc/', views.read_calc)
]