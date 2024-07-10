from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso!.")
            return redirect('crm:home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect('crm:home')
    else:
        return render(request, 'website/pages/home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, "Você saiu.")
    return redirect('crm:home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Você foi cadastrado com sucesso.")
            return redirect('crm:home')
    else:
        form = SignUpForm()
        return render(request, 'website/pages/register.html', {'form': form})

    return render(request, 'website/pages/register.html', {'form': form})


def customer_records(request, pk):
    if request.user.is_authenticated:
        # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'website/pages/record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Você deve estar logado para visualizar esta página.")
        return redirect('crm:home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Registro deletado com sucesso.")
        return redirect('crm:home')
    else:
        messages.success(request, "Você deve estar logado para realizar essa ação.")
        return redirect('crm:home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Registro salvo com sucesso.")
                return redirect('crm:home')
        return render(request, 'website/pages/add_record.html', {'form': form})
    else:
        messages.success(request, "Você deve estar logado para realizar essa ação.")
        return redirect('crm:home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro editado com sucesso.")
            return redirect('crm:home')
        return render(request, 'website/pages/update_record.html', {'form': form})
    else:
        messages.success(request, "Você deve estar logado para realizar essa ação.")
        return redirect('crm:home')
