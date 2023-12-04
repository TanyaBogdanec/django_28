from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, User, Comment
from .forms import TaskForm, CommentForm



# Создайте представление (view) для отображения списка всех задач на главной странице.
# Задачи должны быть отсортированы по дате создания в обратном порядке
# (самые новые задачи должны быть вверху).


def view_task(request):
    tasks = Task.objects.order_by('-date_creation')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)




# Создайте представление (view) для создания новой задачи.
# На странице создания задачи пользователь должен ввести название,
# описание, исполнителя и дату завершения задачи.


def view_create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
        else:
            form = TaskForm()
            return render(request, 'create_task.html', form)




# Реализуйте функциональность назначения задач исполнителям.
# Пользователи должны иметь возможность выбирать исполнителя из списка
# зарегистрированных пользователей при создании задачи.

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', task_id=task.id)
        else:
            form = TaskForm()
            return render(request, 'create_task.html', form)




# Создайте представление (view) для просмотра отдельной задачи.
# Пользователи должны иметь возможность просматривать детали задачи,
# включая описание, исполнителя, статус выполнения и комментарии к задаче.

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', task)




# Реализуйте функциональность обновления статуса выполнения задачи.
# Пользователи должны иметь возможность изменять статус выполнения задачи на "В процессе" и "Завершено".

def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        new_status = request.POST['new_status']
        task.status = new_status
        task.save()
        return redirect('task_detail', task_id=task.id)
    return render(request, 'task_detail.html', task)




# Реализуйте функциональность добавления комментариев к задачам.
# Пользователи должны иметь возможность оставлять комментарии к задачам,
# обсуждать их и отвечать на комментарии других пользователей.

def add_comment_to_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
        return redirect('task_detail', pk=pk)
    else:
        form = CommentForm()
        return render(request, 'add_comment_to_task.html', form)




# Добавьте базовую аутентификацию, чтобы только зарегистрированные пользователи могли создавать задачи,
# назначать исполнителей, изменять статус выполнения и оставлять комментарии.

@login_required
def create_task_post(request):
    if request.method == ('POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            return render(request, 'task_created.html')
    else:
        form = TaskForm()
        return render(request, 'create_task.html', form)

@login_required
def assign_executor(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        executor_id = request.POST.get('executor_id')
        executor = User.objects.get(pk=executor_id)
        return render(request, 'assigned_executor.html', task, executor)
    else:
        users = User.objects.all()
        return render(request, 'assign_executor.html', task, users)


@login_required
def update_status(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        task.status = new_status
        task.save()
        return render(request, 'updated_task_status.html', task, new_status)
    else:
        return render(request, 'update_task_status.html', task)

@login_required
def add_comment_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        new_comment = Comment(text=comment_text, task=task)
        new_comment.save()
        return redirect('task_detail', task_id=task.id)
    else:
        return render(request, 'add_comment_to_task.html', task)


