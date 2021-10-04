from django.urls import path
from .views import BlogListView


app_name = "Blog"
urlpatterns = [
    pach('', BlogListView.as_view(), name="home")
    
]


