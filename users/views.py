from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def my_teacher(request):
    return render(request, 'my_teacher.html')