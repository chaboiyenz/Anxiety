from django.urls import path 
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('', views.home, name="home"),
    path ('navbar/', views.navbar, name="navbar"),
    path ('about/', views.about, name="about"),
    path ('assessment/', views.assessment, name="assessment"),
    path ('contact/', views.contact, name="contact"),
    path ('coping/', views.coping, name="coping"),
    path ('problem/', views.problem, name="problem"),
    path ('problem1/', views.problem1, name="problem1"),
    path ('meaning/', views.meaning, name="meaning"),
    path ('emotion/', views.emotion, name="emotion"),
    path ('social/', views.social, name="social"),
    path ('avoidance/', views.avoidance, name="avoidance"),
    path ('avoidance1/', views.avoidance1, name="avoidance1"),
    path ('avoidance2/', views.avoidance2, name="avoidance2"),
    path ('avoidance3/', views.avoidance3, name="avoidance3"),
    path ('avoidance4/', views.avoidance4, name="avoidance4"),
    path ('signin/', views.signin, name="signin"),
    path ('signup/', views.signup, name="signup"),
    path ('signout/', views.signout, name="signout"),
    path ('updateprofile/', views.updateprofile, name="updateprofile"),
    path ('update/<int:pk>/', views.update, name="update"),
    path ('profile/', views.profile, name="profile"),
    path ('delete/<int:pk>/', views.delete, name="delete"),
    path ('category/', views.category, name="category"),
    path ('feedback/', views.feedback, name="feedback"),
    path ('person/', views.person, name="person"),
    path ('pro/', views.pro, name="pro"),
    path ('mood/', views.mood, name="mood"),
    path ('moodtracker/', views.moodtracker, name="moodtracker"),
    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)