from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404, redirect

from Sensor_Lister.models import Capteur
from Sensor_Lister.forms import RechercheCapteurForm, CapteurForm
from Sensor_Lister.serializers import CapteurSerializer, CapteurDetailSerializer

def capteur_liste(request):
    capteurs = Capteur.objects.all()
    return render(request, 'Sensor_Lister/capteur_liste.html', {'capteurs': capteurs})

def capteur_detail(request, id):
    capteurs = get_object_or_404(Capteur, id=id)
    return render(request, 'Sensor_Lister/capteur_detail.html', {'capteurs': capteurs})

def rechercheCapteur(request):
    # pour afficher tout les capteur par defaut
    capteurs = Capteur.objects.all()

    #verifier si une recherche est effectuee
    if 'q' in request.GET or 'actifs_seulement' in request.GET:
        form = RechercheCapteurForm(request.GET)

        if form.is_valid():
            q = form.cleaned_data['q']
            actifs = form.cleaned_data['actifs_seulement']

            if q:
                capteurs = capteurs.filter(nom__icontains=q)

            if actifs:
                capteurs = capteurs.filter(actif=True)
        else:
            capteurs = Capteur.objects.none()
    else:
        form = RechercheCapteurForm()

    return render(request, 'Sensor_Lister/rechercheCapteur.html', {'form': form, 'capteurs': capteurs})

def capteur_ajouter(request):
    if request.method == 'POST':
        form = CapteurForm(request.POST)
        
        if form.is_valid():
            capteur = form.save()
            return redirect('capteur-detail', capteur.id)
    else:
        form = CapteurForm()

    return render(request, 'Sensor_Lister/capteur_ajouter.html', {'form': form})

def capteur_modifier(request, id):
    capteur = get_object_or_404(Capteur, id=id)
    if request.method == 'POST':
        form = CapteurForm(request.POST, instance=capteur)
        if form.is_valid():
            capteur = form.save()
            return redirect('capteur-detail', capteur.id)
    else:
        form = CapteurForm(instance=capteur)
    
    return render(request, 'Sensor_Lister/capteur_ajouter.html', {'form': form, 'modification': True, 'capteur': capteur})

def capteur_supprimer(request, id):
    capteur = get_object_or_404(Capteur, id=id)
    if request.method == 'POST':
        capteur.delete()
        return redirect('capteur-liste')
    
    return render(request, 'Sensor_Lister/capteur_supprimer.html', {'capteur': capteur})

def page_principale(request):
    return render(request, 'Sensor_Lister/page_principale.html')

class CapteurViewset(ReadOnlyModelViewSet):

    serializer_class = CapteurSerializer
    def get_queryset(self):
        return Capteur.objects.all()

class CapteurDetailViewset(ReadOnlyModelViewSet):

    serializer_class = CapteurDetailSerializer
    def get_queryset(self):
        return Capteur.objects.all()