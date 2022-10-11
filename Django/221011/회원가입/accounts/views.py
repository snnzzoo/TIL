from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
# from accounts.models import User
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def list(request):
    users = get_user_model().objects.order_by('-pk')
    context = {
        'users': users
    }
    return render(request, 'accounts/list.html', context)

def detail(request, pk):
    # 유저를 참조할 때는 상속을 받고 있기 때문에 get_user_model을 import해서 함수로 참조
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)