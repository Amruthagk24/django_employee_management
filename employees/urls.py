from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('emp_home/',views.emp_home),
    path('empsignup/',views.emp_signup),
    path('signups/',views.lg),
    path('emplogins/',views.emp_login),
    path('emplog/',views.empdologin),
    path('viewallemps/',views.show),
    path('emp_edit/<str:id>',views.edit),
    path('emp_edit_post/',views.edit_post),
    path('emp_delete/<str:id>', views.emp_del),]