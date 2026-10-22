from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import  redirect
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task






def indexView(request):

    return render(request, 'Index.html')




def RegisterView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            messages.success(request, 'Registration successful')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'Register.html', {'form': form})












def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')






def LogOutView(request):

    logout(request)

    return redirect('/')








@login_required(login_url="loginF")
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})



# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import Task
# from .filters import TaskFilter
#
#
# @login_required
# def task_list(request):
#     tasks = Task.objects.filter(
#         user=request.user
#     ).order_by('-created_at')
#
#     task_filter = TaskFilter(
#         request.GET,
#         queryset=tasks
#     )
#
#     return render(request, 'task_list.html', {
#         'tasks': task_filter.qs,
#         'filter': task_filter,
#     })

#
# @login_required
# def task_list(request):
#     tasks = Task.objects.filter(user=request.user).order_by('-created_at')
#
#     return render(request, 'task_list.html', {'tasks': tasks})


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Task
from .filters import TaskFilter

@login_required(login_url="loginF")
def task_list(request):
    tasks = Task.objects.filter(
        user=request.user
    ).order_by('-created_at')

    task_filter = TaskFilter(
        request.GET,
        queryset=tasks
    )

    filtered_tasks = task_filter.qs

    paginator = Paginator(filtered_tasks, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'task_list.html', {
        'tasks': page_obj,
        'page_obj': page_obj,
        'filter': task_filter,
    })



@login_required(login_url="loginF")
def delete_task(request, task_id):

    data = Task.objects.get(id=task_id)

    data.delete()

    return redirect('task_list')





@login_required
def toggle_task_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(
            Task,
            id=task_id,
            user=request.user
        )

        task.completed = not task.completed
        task.save()

    return redirect('task_list')









@login_required
def edit_task(request, task_id):
    task =  Task.objects.get(id=task_id,
        user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {
        'form': form,
        'task': task
    })





@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)

    return render(request, 'task_details.html', {
        'task': task
    })
