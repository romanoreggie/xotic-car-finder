from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
    path('<int:car_id>/', views.onecar, name='onecar'),
	path('post_url/', views.post_car, name='post_car'),
	path('user/<username>/', views.profile, name='profile'),
	path('login/', views.login_view, name='login'),
	path('show/', views.show, name='show'),
	path('logout/', views.logout_view, name='logout'),
	path('signup/', views.signup_view, name='signup'),
]
