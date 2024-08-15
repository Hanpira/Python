from django.shortcuts import render, get_object_or_404, redirect

# Базовый класс для обработки страниц с формами.
from django.views.generic.edit import FormView
# Спасибо django за готовую форму регистрации.
from django.contrib.auth.forms import UserCreationForm

# Спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа.
# По нему django будет определять,
# выполнил ли вход пользователь.
from django.contrib.auth import login

# Для Log out с перенаправлением на главную
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

# Для смены пароля - форма
from django.contrib.auth.forms import PasswordChangeForm

from datetime import datetime
# для ответа на асинхронный запрос в формате JSON
from django.http import JsonResponse 
import json

# Create your views here.
from .models import Plant

# базовый URL приложения, главной страницы -
# часто нужен при указании путей переадресации
app_url = "/plants/"

def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_riddles и message
    return render(
        request,
        "index.html",
        {
            "latest_plants":
                Plant.objects.order_by('-pub_date')[:15],
            "message": message
        }
    )

def detail(request, plant_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "plcard.html",
        {
            "plant": get_object_or_404(Plant, pk=plant_id),
            "error_message": error_message
        }
    )

# наше представление для регистрации
class RegisterFormView(FormView):
    # будем строить на основе
    # встроенной в django формы регистрации
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь
    # в случае успешной регистрации.
    # В данном случае указана ссылка на
    # страницу входа для зарегистрированных пользователей.
    success_url = app_url + "login/"
    # Шаблон, который будет использоваться
    # при отображении представления.
    template_name = "reg/register.html"
    def form_valid(self, form):
        # Создаём пользователя,
        # если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

# наше представление для входа
class LoginFormView(FormView):
    # будем строить на основе
    # встроенной в django формы входа
    form_class = AuthenticationForm
    # Аналогично регистрации,
    # только используем шаблон аутентификации.
    template_name = "reg/login.html"
    # В случае успеха перенаправим на главную.
    success_url = app_url
    def form_valid(self, form):
        # Получаем объект пользователя
        # на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

# для выхода - миниатюрное представление без шаблона -
# после выхода перенаправим на главную
class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя,
        # запросившего данное представление.
        logout(request)
        # После чего перенаправляем пользователя на
        # главную страницу.
        return HttpResponseRedirect(app_url)

# наше представление для смены пароля
class PasswordChangeView(FormView):
    # будем строить на основе
    # встроенной в django формы смены пароля
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    # после смены пароля нужно снова входить
    success_url = app_url + 'login/'
    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)

def admin(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону admin.html
    # с заданными параметрами latest_riddles и message
    return render(
        request,
        "admin.html",
        {
            "latest_plants":
                Plant.objects.order_by('-pub_date')[:15],
            "message": message,
        }
    )

#обработка отправляемых заполненных форм
def post_plant(request):
    # защита от добавления загадок неадминистраторами
    author = request.user
    if not (author.is_authenticated and author.is_staff):
        return HttpResponseRedirect(app_url+"admin")
    # добавление загадки
    rid = Plant()
    rid.plant_name = request.POST['textName']
    rid.plant_type = request.POST['textType']
    rid.plant_number = request.POST['number']
    rid.pub_date = datetime.now()
    rid.save()
    return HttpResponseRedirect(app_url+str(rid.id))

