from django.urls import path
from .views import home_view, about_view, contact_view, my_self_view, my_teacher_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('my_self/', my_self_view, name='my_self' ),
    path('my_teacher/', my_teacher_view, name='my_teacher'),

]