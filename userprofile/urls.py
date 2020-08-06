from django.urls import path

from .views import home, detail, register, signup, UserDetailView

app_name = "userprofile"
urlpatterns = [
    path('', home, name="home"),
    path('<int:pk>/detail/', UserDetailView.as_view(), name='detail'),
    path('signup/', signup, name="signup"),
    path('register/', register, name="register"),

]