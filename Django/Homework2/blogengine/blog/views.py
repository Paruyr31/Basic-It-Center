from django.shortcuts import render
from .models import Students
# Create your views here.
def students(request):
    student = Students.objects.all()
    return render(request, 'blog/index.html', context={"students": student})