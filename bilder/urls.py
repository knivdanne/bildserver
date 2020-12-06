from django.urls import path

from . import views

app_name = 'bilder'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('', views.SaveProfile, name='saved'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]