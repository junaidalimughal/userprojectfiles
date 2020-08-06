from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.mail import send_mail

from django.views.defaults import page_not_found
from django.views.generic.detail import DetailView

from .forms import CustomUserCreationForm, SignUp
from .models import CustomUser

def home(request):
    users = CustomUser.objects.all()

    return render(request, "userprofile/home.html", {"users":users})

class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "userprofile/detail.html"  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def detail(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    user = [(key, value) for key, value in user.__dict__.items()]
    print(user)
    return render(request, "userprofile/detail.html", {"user":user})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('User Sign up', 'Thank you for signing up ' + str(form.cleaned_data['email']), 'junaidali0300@gmail.com', [str(form.cleaned_data['email'])], fail_silently=False)
            messages.success(request, "Account created successfully.")
            return redirect('userprofile:register')
    else:
        form = CustomUserCreationForm()

    return render(request, 'userprofile/register.html', {"form":form})

def signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            send_mail('User Sign up', 'Thank you for signing up ' + str(form.cleaned_data['email']), 'junaidali0300@gmail.com', [str(form.cleaned_data['email'])], fail_silently=False)
            return redirect('userprofile:register')
    else:
        form = SignUp()

    return render(request, "userprofile/register.html", {"form":form})

def error_404(request, exception):
    if request.path.endswith("/detail/"):
        template_name = 'error/404.html'
    return page_not_found(request, exception, template_name=template_name)