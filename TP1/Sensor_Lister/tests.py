from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from Sensor_Lister.models import Capteur

class TestCategory(APITestCase):
    url = reverse_lazy('capteur-liste')
    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        capteur = Capteur.objects.create(nom='Temp-garage', type_capteur='T', actif=True)
        Capteur.objects.create(nom='Temp-gym', type_capteur='T', actif=False)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                'id': capteur.pk,
                'nom': capteur.nom,
                'type_capteur': capteur.type_capteur,
                'actif': capteur.actif
            }
        ]
        self.assertEqual(expected, response.json())

    def test_create(self):
        self.assertFalse(Capteur.objects.exists())
        response = self.client.post(self.url, data={'nom': 'Nouvelle categorie'})

        self.assertEqual(response.status_code, 405)
        self.assertFalse(Capteur.objects.exists())
