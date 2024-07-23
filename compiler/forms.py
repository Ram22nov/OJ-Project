from django import forms
from compiler.models import CodeSubmission

LANGUAGE_CHOICES = [
    ("cpp", "C++"),
    ("py", "Python"),
    ("c", "C"),
]


class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES)

    class Meta:
        model = CodeSubmission
        fields = ["language", "code", "input_data"]