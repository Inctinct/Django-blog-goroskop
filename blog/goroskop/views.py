from django.shortcuts import render, redirect
from .models import Goroskop
from .forms import GoroskopForm
from django.utils import timezone


def goroskop(request):
    return render(request,'goroskop/goroskop.html')


def kozerog(request):
    goros = Goroskop.objects.filter(title = 'Козерог')
    return render(request,'goroskop/znak.html', {'goros': goros})


def vodolei(request):
    goros = Goroskop.objects.filter(title = 'Водолей')
    return render(request,'goroskop/znak.html', {'goros': goros})


def ribi(request):
    goros = Goroskop.objects.filter(title = 'Рыбы')
    return render(request,'goroskop/znak.html', {'goros': goros})


def oven(request):
    goros = Goroskop.objects.filter(title = 'Овен')
    return render(request,'goroskop/znak.html', {'goros': goros})


def telec(request):
    goros = Goroskop.objects.filter(title = 'Телец')
    return render(request,'goroskop/znak.html', {'goros': goros})


def bliznici(request):
    goros = Goroskop.objects.filter(title = 'Близнецы')
    return render(request,'goroskop/znak.html', {'goros': goros})


def rak(request):
    goros = Goroskop.objects.filter(title = 'Рак')
    return render(request,'goroskop/znak.html', {'goros': goros})


def lev(request):
    goros = Goroskop.objects.filter(title = 'Лев')
    return render(request,'goroskop/znak.html', {'goros': goros})


def deva(request):
    goros = Goroskop.objects.filter(title = 'Дева')
    return render(request,'goroskop/znak.html', {'goros': goros})


def vesi(request):
    goros = Goroskop.objects.filter(title = 'Весы')
    return render(request,'goroskop/znak.html', {'goros': goros})


def skorpion(request):
    goros = Goroskop.objects.filter(title = 'Скорпион')
    return render(request,'goroskop/znak.html', {'goros': goros})


def strelec(request):
    goros = Goroskop.objects.filter(title = 'Стрелец')
    return render(request,'goroskop/znak.html', {'goros': goros})


def create_goros(request):
    if request.method == 'POST':
        form = GoroskopForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('goroskop')
    else:
        form = GoroskopForm()
    return render(request, 'goroskop/create_goros.html', {'form':form})