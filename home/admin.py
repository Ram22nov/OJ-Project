from django.contrib import admin
from .models import Problem



class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty')
    fields = ('title', 'description', 'difficulty', 'input_data', 'expected_output')

admin.site.register(Problem, ProblemAdmin)
