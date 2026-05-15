from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Отправка приветственного письма
            send_mail(
                'Добро пожаловать на наш сайт!',
                'Спасибо за регистрацию на нашем сайте.',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return redirect('product_list')  # Убедитесь, что 'product_list' - это имя существующего маршрута
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
