from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from .forms import RegistrationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from post.models import Post

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))
 
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            accounts = authenticate(email=email, password=raw_password)
            #login(request, accounts)
            destination = kwargs.get("next")
            #destination = get_redirect_if_exists(request)
            if destination: # if destination != None
                return redirect(destination)
            return redirect('/')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
 
    return render(request, 'accounts/register.html', context)
 
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')
 
def login_view(request, *args, **kwargs):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'accounts/login.html')
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'accounts/login.html')


def update(request, pk):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user) # 이게 없으면 수정할 때마다 새로운 계정을 만든다.
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)
 
def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect

@login_required
def change_password(request,pk):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호를 바꾸면 기존 세션과 일치하지 않게 되어 로그아웃된다. 이를 방지하기 위한 auth_hash 갱신.
            update_session_auth_hash(request, user)  
            return redirect('/')
    
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html',{'form':form})

@login_required
def delete(request) :
    user = request.user
    user.delete()
    return redirect('/')

@login_required
def profile_register(request, post_pk, user_pk):
    user_list = get_user_model().objects.all()
    user = get_user_model()
    person = get_object_or_404(user, pk=user_pk)
    post = Post.objects.get(id=post_pk)
    context={
        'user_list' : user_list,
        'person' : person,
        'post' : post
    }
    return render(request, 'accounts/profile_register.html', context)