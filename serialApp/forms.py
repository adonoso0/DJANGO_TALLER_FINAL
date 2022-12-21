from django import forms
from serialApp.models import Inscritos, Instituciones

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class NumberInput(forms.NumberInput):
    input_type = 'number'

class FormInscritos(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, max_length=50)
    telefono = forms.IntegerField(min_value=900000000, max_value=999999999, label='Teléfono')
    fechareserva = forms.DateField(widget=DateInput, label='Fecha de reserva')
    horareserva = forms.TimeField(widget=TimeInput, label='Hora de reserva')
    observacion = forms.CharField(required=False, label='Observación')
    
    class Meta:
        model = Inscritos
        fields = '__all__'

class FormInstituciones(forms.ModelForm):
    
    nombre = forms.CharField(min_length=2, max_length=20)
    
    class Meta:
        model = Instituciones
        fields = '__all__'
