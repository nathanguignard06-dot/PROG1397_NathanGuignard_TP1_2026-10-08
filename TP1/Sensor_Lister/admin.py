from django.contrib import admin

from Sensor_Lister.models import Capteur, Location

class CapteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_capteur', 'actif', 'emplacement')

admin.site.register(Capteur, CapteurAdmin)
admin.site.register(Location)
