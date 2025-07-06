from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def my_self_view(request):
    return render(request, 'my_self.html')


def my_teacher_view(request):
    return render(request, 'my_teacher.html')
