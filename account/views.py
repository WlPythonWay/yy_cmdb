from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def cmdb_login(request):
    context = {'error_message': ''}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home:index')
            else:
                print('未激活')
                context['error_message'] = '用户未激活'
                return render(request, 'account/login.html', context)

        else:
            context['error_message'] = '用户名或密码错误'
            return render(request, 'account/login.html', context)

    return render(request, 'account/login.html', context)


def cmdb_logout(request):
    logout(request)
    return redirect('account:login')


@login_required
def my_page(request):
    context = {'user': request.user, 'error_message': ''}
    if request.method == 'POST':
        username = request.user
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']
        print(username, password, confirm_password)
        if password == confirm_password:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return redirect('account:login')
        else:
            error_message = '两次密码不一致'
            context['error_message'] = error_message
    return render(request, 'account/user_profile.html', context)


@login_required
def user_manager(request):
    user = User.objects.all()
    context = {'users': user, 'current_user': request.user}
    if request.method == 'GET':
        username = request.GET.get('username', '')
        if username:
            User.objects.get(username=username).delete()
            return HttpResponse("ok")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST['confirmPassword']
        print(username, password, confirm_password)
        if password == confirm_password:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
        else:
            print('两次密码不一致')

    return render(request, 'account/user_manager.html', context)


@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        print(user)
        user.save()

    return redirect('account:manager')


def test(request):
    return render(request, 'account/test.html')
