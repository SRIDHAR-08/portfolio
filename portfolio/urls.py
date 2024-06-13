from django.urls import path
from .views import *
urlpatterns = [
    path('',portfolio_home , name='portfolio_home'),
    path('allproject',allproject , name='allproject'),
    path('resume_data',resume_data , name='resume_data'),
    path('contect',Contect , name='contect'),
    path('mes_succ',mes_succ , name='mes_succ'),
    path('project_details/<int:id>',project_details , name='project_details'),
    path('portfolio_about',portfolio_about , name='portfolio_about'),
]

