from django.contrib import admin
from .models import Problem
from .models import Feedback
from django import forms


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty')
    fields = ('title', 'description', 'difficulty', 'input_data', 'expected_output')

admin.site.register(Problem, ProblemAdmin)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'feedback_text']  # Adjust fields as necessary

class FeedbackAdmin(admin.ModelAdmin):
    form = FeedbackForm
    list_display = ('user', 'feedback_text', 'created_at')
    search_fields = ('feedback_text', 'user__username')
    list_filter = ('created_at', 'user')

admin.site.register(Feedback, FeedbackAdmin)