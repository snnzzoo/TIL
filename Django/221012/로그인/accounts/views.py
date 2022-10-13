from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    users = get_user_model().objects.order_by('-pk')
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)


def signup(request):
    # 이미 로그인한 사람은 다시 회원가입 할 수 없도록
    if request.user.is_authenticated:
        return redirect('articles:index')
    else:
        # POST 요청 처리
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                # 회원가입 후 곧바로 로그인 진행
                user = form.save()
                auth_login(request, user)
                return redirect('accounts:index')
        else:
            form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)


def login(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('articles:index')

@login_required
# 로그인이 필요한 상황에서 사용
# request.user로 유저 객체를 쓰는 view 함수에서는 무조건 쓰는 것이 좋다.
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def logout(request):
    auth_logout(request)
    return redirect('index')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # 암호 변경 시 세션 무효화 방지하기
            update_session_auth_hash(request, form.user)
            return redirect('accounts:detail', request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
def delete(request):
    # 선 탈퇴
    request.user.delete()
    # 후 로그아웃
    auth_logout(request)
    return redirect('index')