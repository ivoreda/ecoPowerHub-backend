from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectListView.as_view(), name='home'),
    path('projects/create/', views.ProjectCreateView.as_view(),
         name='project-create'),
    path('myprojects/', views.UserSpecificProjectView.as_view(), 
          name='user-projects'),
    path('projects/<uuid:pk>/', views.ProjectDetailView.as_view(),
         name='project-detail'),
    path('projects/update/<uuid:pk>/',
         views.ProjectUpdateView.as_view(), name='project-update'),
    path('projects/delete/<uuid:pk>/',
         views.ProjectDeleteView.as_view(), name='project-delete'),

    path('projects/buy/<uuid:pk>/', views.BuyProjectView.as_view(), name='buy-project'),

    path('projects/invest/', views.InvestView.as_view(), name='invest'),
]
