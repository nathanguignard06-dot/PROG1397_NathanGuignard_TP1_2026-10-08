from rest_framework.serializers import ModelSerializer

from Sensor_Lister.models import Capteur

class CapteurSerializer(ModelSerializer):
    class Meta:
        model = Capteur
        fields = ['id', 'nom']

class CapteurDetailSerializer(ModelSerializer):
    class Meta:
        model = Capteur
        fields = ['nom', 'type_capteur', 'actif', 'detail']