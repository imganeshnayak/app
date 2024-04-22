from django.shortcuts import redirect, render
from feedback.models import feedback
from django.http import HttpResponse

def index(request):
    mem = feedback.objects.all()
    return render(request, 'index.html', {'xy': mem})

def add(request):
    return render(request, 'post.html')

def post(request):
    if request.method == "POST":
        course = request.POST.get('course') 
        section = request.POST.get('section')
        semester = request.POST.get('semester')
        Feedback = request.POST.get('Feedback')
        grading = request.POST.get('grading')
        batch = request.POST.get('batch')       
        mem = feedback(course=course, section=section, semester=semester, Feedback=Feedback, grading=grading, batch=batch)
        mem.save()
        return render(request, 'index.html', {'xy': feedback.objects.all()})  # Redirect to index.html after saving data
    else:
        return render(request, 'post.html')  # Render the form for GET requests

def delete(request,id):
    if request.method =="GET":
        mem=feedback.objects.get(id=id)
        mem.delete()
        return render(request,"index.html")
    else:
        return render(request, 'post.html')  # Render the form for GET requests

