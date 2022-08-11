from django.urls import path

from . import views

urlpatterns = [
    path('ind', views.index, name='index'),
    path('ss', views.sara, name='sara'),
    path('getquestion/<int:question_id>/', views.question, name='question'),
    path('login_user/',views.login_user,name='login_user'),
    path('election/',views.election,name='election'),
    path('getpeople_All/',views.getpeople_All,name='getpeople_All'),   
    path('getcandidates_All/',views.getcandidates_All,name='getcandidates_All'),
    path('getelection_All/',views.getelection_All,name='getelection_All'),
    path('getparties_All/',views.getparties_All,name='getparties_All'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('getelectioncount/', views.getelectioncount, name='getelectioncount'),
    path('ok/', views.ok, name='ok'),

]
