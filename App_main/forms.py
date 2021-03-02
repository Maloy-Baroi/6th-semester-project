from django.contrib.auth.forms import forms
from App_main.models import Routine, ClassVideo, ClassNotes


class RoutineUploadForm(forms.ModelForm):
    Department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Department'}))

    class Meta:
        model = Routine
        exclude = ('Author', )


class ClassVideoUploadForm(forms.ModelForm):
    class Meta:
        model = ClassVideo
        exclude = ('Teacher', )


class ClassNotesUploadForm(forms.ModelForm):
    Notes = forms.FileField(required=True, widget=forms.TextInput(attrs={'type': 'file'}))

    class Meta:
        model = ClassNotes
        exclude = ('Teacher', )


