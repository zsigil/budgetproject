from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Project

# Create your views here.
def project_list(request):
    return render(request, 'budget/project_list.html')

def project_detail(request, projectslug):
    project = get_object_or_404(Project, slug=projectslug)
    expense_list = project.expenses.all()
    return render(request, 'budget/project_detail.html', {'project':project, 'expense_list':expense_list})
