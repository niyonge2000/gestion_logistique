from django.forms import ModelForm
from app.models import Transfert

class TransfertForm(ModelForm):
    class Meta:
        model = Transfert
        fields = '__all__'
