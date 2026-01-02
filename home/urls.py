from django.urls import path
from . import views


# Step 1: “Configuring the about URL

urlpatterns = [
    path('', views.index, name="home.index"),
    path ('about',views.about, name = 'home.about' )]


