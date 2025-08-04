from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Item
from .forms import ItemForm
from django.db.models import Q

def home(request):
    
    items = Item.objects.all()
    return render(request, 'lostfound_app/home.html', {'items': items})

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'lostfound_app/signup.html', {'form': form})

def user_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'lostfound_app/login.html', {'form': form})

@login_required
def user_logout(request):

    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def post_lost(request):
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.post_type = 'lost'
            item.save()
            messages.success(request, 'Lost item posted successfully!')
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'lostfound_app/post_lost.html', {'form': form})

@login_required
def post_found(request):
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.post_type = 'found'
            item.save()
            messages.success(request, 'Found item posted successfully!')
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'lostfound_app/post_found.html', {'form': form})

def item_detail(request, item_id):
    
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'lostfound_app/item_detail.html', {'item': item})

@login_required
def my_posts(request):
    
    items = Item.objects.filter(user=request.user)
    return render(request, 'lostfound_app/my_posts.html', {'items': items})

@login_required
def delete_item(request, item_id):
    
    item = get_object_or_404(Item, id=item_id)
    if item.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this post.")
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('my_posts')
    
    return render(request, 'lostfound_app/delete_confirm.html', {'item': item})

def search_items(request):
    
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )
    else:
        items = Item.objects.all()
    return render(request, 'lostfound_app/home.html', {'items': items, 'query': query})
