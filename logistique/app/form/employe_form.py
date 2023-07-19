from django.forms import ModelForm
from app.models import Employe

class EmployeForm(ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
