from django.shortcuts import render
from .models import Name


def home(request):

    if request.method == "POST":
        print("here!")
        if request.POST["name"] == "a":
            print("deleted!")
            Name.objects.all().delete()
            return render(request, 'home.html')

    elif Name.objects.all().exists():
        return render(request, 'home.html', {'name': Name.objects.first().name})
    

    elif Name.objects.all().exists():
        return render(request, 'home.html', {'name': Name.objects.first().name})

    else:
        return render(request, 'home.html')


def name(request):
    user = Name(name=request.POST['name'])
    user.save()
    return render(request, 'home.html', {'name': user.name})

def profile(request):
    return render(request, 'profile.html')


def week(request):
    return render(request, 'week.html')


def key(request):
    return render(request, 'key.html')
