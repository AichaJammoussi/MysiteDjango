from django.urls import path
from .views import ListePosts, DetailPost, CreerPost, ModifierPost, SupprimerPost

urlpatterns = [
    path('', ListePosts.as_view(), name='liste_Posts'), 
    path('<int:pk>/', DetailPost.as_view(), name='detail_Post'),
    path('ajouter/', CreerPost.as_view(), name='creer_Post'),
    path('<int:pk>/modifier/', ModifierPost.as_view(), name='modifier_Post'),
    path('<int:pk>/supprimer/', SupprimerPost.as_view(), name='supprimer_Post'),
]
