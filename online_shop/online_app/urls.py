from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

app_name = 'online_app'

urlpatterns = [
        path('', views.home_page_views, name="home_page"),
        path('items/', views.items_views, name="items"),
        path('up_items/', views.upload_item_view, name='upload_item'), 
        # New signs for accounts:
        path('signup/', views.signup_view, name='signup'), 
        path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # Use Django's built-in login
        path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Use Django's built-in logout
        path('item/<int:pk>/', views.item_detail, name='item_detail'), 
    ]
