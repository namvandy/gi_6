from django.forms import ModelForm

from projectapp.views import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','image','description']
