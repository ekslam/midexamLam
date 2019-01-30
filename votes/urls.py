from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:votes_id>/', views.candidate_detail, name='detail'),
    #path('<int:votes_id>/update', views.update, name='update'),
    path('create/', views.candidate_create, name = 'create'),
    path('position/', views.position_create, name = 'position'),

]
