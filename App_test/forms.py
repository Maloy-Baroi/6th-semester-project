from django.contrib.auth.forms import forms
from App_test.models import MCQ


class MCQForm(forms.ModelForm):

    class Meta:
        model = MCQ
        fields = "__all__"

