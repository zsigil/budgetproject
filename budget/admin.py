from django.contrib import admin
from .models import Project, Category, Expense
# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Expense)
