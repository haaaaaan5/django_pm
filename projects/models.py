from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.
class ProjectsStatus(models.IntegerChoices):
    PENDING=1,'pending'
    COMPLETED=2,'completed'
    POSTPONED=3,'postponed'
    CANCELED=4,'canceled'
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title=models.CharField(max_length=255)
    desciption=models.TextField()
    status=models.IntegerField(choices=ProjectsStatus.choices,default=ProjectsStatus.PENDING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    user= models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Task(models.Model):
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    Project=models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.description
