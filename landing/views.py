from django.shortcuts import render
from .forms import SubscribersForm


def landing(request):
    name = 'Pit'
    current_date = '23.09.17'
    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    return render(request, 'landing/home.html', locals())