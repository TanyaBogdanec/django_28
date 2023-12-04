from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    email = models.EmailField(max_length=250, verbose_name="email")
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = [
        ("In progress", "In progress"),
        ("Completed", "Completed")
    ]

    name_task = models.CharField(max_length=100, verbose_name="name_task")
    description = models.TextField()
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)


    def __str__(self):
        return self.name_task


class Comment(models.Model):
    task_comment = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)