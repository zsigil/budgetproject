from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .forms import ProjectCreateForm
from django.http import HttpResponseRedirect
from django.utils.text import slugify

from .models import Project, Category

# Create your views here.
def project_list(request):
    return render(request, 'budget/project_list.html')


def project_detail(request, projectslug):
    project = get_object_or_404(Project, slug=projectslug)
    expense_list = project.expenses.all()
    return render(request, 'budget/project_detail.html', {'project':project, 'expense_list':expense_list})


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name='budget/add_project.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')

        for category in categories:
            Category.objects.create(
                project = Project.objects.get(id=self.object.id),
                name = category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
