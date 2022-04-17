from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': '와우 첫번째'},
    {'id': 2, 'name': '와우 두번째'},
    {'id': 3, 'name': '와우 셋번째'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
