from django.shortcuts import render

from team.models import Category, Press

def team(request):
    return render(request, 'team.html')

def press(request):
    presss = Press.objects.all().order_by("-created_on")
    context = {"presss": presss}
    return render(request, 'press.html', context)

# Create your views here.
