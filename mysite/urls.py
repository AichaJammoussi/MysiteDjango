from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('jeux/', include('jeux.urls')),
    path('blog/', include('blog.urls')),

    path('', views.index, name='index'),  # accueil/home

    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/Login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/Logout.html'), name='logout'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



















'''
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin, auth
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/',include('magasin.urls')),
    path('jeux',include('jeux.urls')),
    path('', views.index, name='index'),#accueil/home

    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/Login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Logout.html'), name = 'logout'),

] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)'''