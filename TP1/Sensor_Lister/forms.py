from django import forms
from Sensor_Lister.models import Capteur


class RechercheCapteurForm(forms.Form):
    q = forms.CharField(max_length=40, label="Nom du capteur", required=False)
    actifs_seulement = forms.BooleanField(required=False, label="Actifs seulement")

class CapteurForm(forms.ModelForm):
    class Meta:
        model = Capteur
        fields = '__all__'