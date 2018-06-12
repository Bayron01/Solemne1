from django.forms import ModelForm
from Baloncesto.models import Jugador
from Baloncesto.models import Entrenador
from Baloncesto.models import Equipo
from Baloncesto.models import Nomina

class JugadorForm(ModelForm):
    class Meta:
        model = Jugador
        fields = ['name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position']


class EntrenadorForm(ModelForm):
	class Meta:
		model = Entrenador
		fields = ['name', 'age', 'email', 'nickname', 'rut']


class EquipoForm(ModelForm):
	class Meta:
		model = Equipo
		fields = ['name', 'description', 'logo', 'code']


class NominaForm(ModelForm):
	class Meta:
		model = Nomina
		fields = ['name', 'date', 'time']


