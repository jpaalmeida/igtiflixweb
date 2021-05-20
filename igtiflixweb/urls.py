from django.contrib import admin
from django.urls import path, include
from .views import ridirect_root

urlpatterns = [
    #path('', view=include('principal.urls')),
    path('', ridirect_root),
    path('admin/', admin.site.urls),
    path(route='principal/', view=include('principal.urls')),
    path(route='genero/', view=include('genero.urls')),
    path(route='serie/', view=include('serie.urls'))
]
