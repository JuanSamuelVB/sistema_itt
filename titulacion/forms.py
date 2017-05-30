from bootstrap_datepicker.widgets import DatePicker
from django import forms
from .models import Titulacion

class TitulacionForm(forms.ModelForm):
    class Meta:
        model = Titulacion
        fields = ['proyecto', 'alumno', 'presidente', 'secretario', 'vocal', 'suplente', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateField(
          widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True})),
            'fecha_fin': forms.DateField(
          widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True})),
        }
