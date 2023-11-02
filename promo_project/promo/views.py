from django.shortcuts import render, redirect
from .forms import PersonForm, CampaignForm, HouseForm
from .models import Person, Campaign, House
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешной регистрации
    else:
        form = ProfileForm()
    return render(request, 'promo/register.html', {'form': form})

def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного создания кампании
    else:
        form = CampaignForm()
    return render(request, 'promo/create_campaign.html', {'form': form})

def add_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешного добавления дома
    else:
        form = HouseForm()
    return render(request, 'promo/add_house.html', {'form': form})

def home(request):
    return render(request, 'promo/home.html')

@login_required  # Обязательная авторизация для доступа к странице профиля
def profile(request):
    user = request.user
    return render(request, 'promo/profile.html', {'user': user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('promo:profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'promo/edit_profile.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'promo/login.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'promo/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')