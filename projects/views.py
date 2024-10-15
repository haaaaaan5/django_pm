
from . import models
from . import form
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
# Create your views here.
class ProjectListview(ListView):
    model=models.Project
    template_name='project/list.html'
class ProjectCreateview(CreateView):
    model=models.Project
    form_class=form.ProjectCreateForm
    template_name='project/create.html'
    success_url=reverse_lazy('project_list')
