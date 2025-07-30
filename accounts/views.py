from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST) # faz a validação do formulário
        if user_form.is_valid():
            user_form.save()
            return redirect('bikes_list')  # redireciona para a página de login após o registro
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})
