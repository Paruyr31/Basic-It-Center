from . import views
from django.urls import path
from django.conf.urls import url

app_name = "blog"
urlpatterns = [
    #path('', views.post_list, name="post_list"),
    path('<int:y>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name="post_detail"),
    #path('hello/', views.hello),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('', views.dashboard, name='dashboard'),
]

