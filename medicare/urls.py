from django.urls import path
from medicapp import views
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('patient/', views.patient_home, name='patient'),
    path('logout/', views.user_logout, name='logout'),
    path('accounts/', include('allauth.urls')),  # AUTHENTICATION
    path('login/', include('allauth.socialaccount.urls')),  # for social account URLs
    path('create_profile/', views.create_profile, name='create_profile'),
    #path('diagnosis/', views.diagnosis, name='diagnosis'),
    

    #PASSWORD RESET
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]
