from django.shortcuts import render,redirect
from .forms import applyForm,ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return render(request, 'projects.html')
def apply(request):
    return render(request, 'apply.html')


def apply_view(request):
    if request.method=="POST":
        Ap=applyForm(request.POST)
        if Ap.is_valid():
            balwa=Ap.save(commit=False)
            balwa.user=request.user
            balwa.save()
            return redirect('home')
        
    else:
        Ap=applyForm()

    return render(request,'apply.html',{'Ap':Ap})


def contact_view(request):
    if request.method=="POST":
        con=ContactForm(request.POST)
        if con.is_valid():
            bal=con.save(commit=False)
            bal.user=request.user
            bal.save()
            return redirect('home')
        
    else:
        con=ContactForm()

    return render(request,'contact.html',{'con':con})
