from django.shortcuts import render
from .models import Menu, Setting, Incident



def index(request):
    menu = Menu.objects.all()
    setting = Setting.objects.all()
    render_dict = {
        'menulist': menu,
        'settinglist': setting,
        'dashboard-data': []
    }
    return render(request, 'index.html', render_dict)