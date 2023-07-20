from django.shortcuts import render
from django.http import JsonResponse
from .models import Gol
from django.db.models.functions import Lower

# Create your views here.

def ricerca_gol(request):
    if request.method == 'POST':
        nomeGiocatore = request.POST.get('nomeGiocatore','')
        squadra = request.POST.get('squadra','')
        competizione = request.POST.get('competizione','')
        giornata = request.POST.get('giornata','')
        descrizioneGoal = request.POST.get('descrizioneGoal','')
        valutazione = request.POST.get('valutazione','')
        stagione = request.POST.get('stagione','')

        goal = Gol.objects.filter(
            nomeGiocatore__icontains=nomeGiocatore,
            squadra__icontains=squadra,
            competizione__icontains=competizione,
            giornata__icontains=giornata,
            descrizioneGoal__icontains=descrizioneGoal,
            valutazione__icontains=valutazione,
            stagione__icontains=stagione
        ).order_by('data','ora','minutoGoal')

        for goal1 in goal:
            goal1.video += "&mute=1&autoplay=1"
            goal1.save()

        context = {'goal': goal, 'nomeGiocatore': nomeGiocatore, 'squadra': squadra, 'competizione': competizione,
                   'giornata': giornata, 'descrizioneGoal': descrizioneGoal, 'valutazione': valutazione,
                   'stagione': stagione}
        return render(request, 'gols/visualizza_gol.html', context)
    else:
        giocatori = Gol.objects.order_by(Lower('nomeGiocatore')).values_list('nomeGiocatore', flat=True).distinct()
        squadre = Gol.objects.order_by(Lower('squadra')).values_list('squadra', flat=True).distinct()
        competizioni = Gol.objects.order_by(Lower('competizione')).values_list('competizione', flat=True).distinct()
        giornate = Gol.objects.order_by(Lower('giornata')).values_list('giornata', flat=True).distinct()
        descrizioni = Gol.objects.order_by(Lower('descrizioneGoal')).values_list('descrizioneGoal', flat=True).distinct()
        valutazioni = Gol.objects.order_by(Lower('valutazione')).values_list('valutazione', flat=True).distinct()
        stagioni = Gol.objects.order_by(Lower('stagione')).values_list('stagione', flat=True).distinct()
        context = {'giocatori': giocatori, 'squadre': squadre, 'competizioni': competizioni, 'giornate': giornate,
                   'descrizioni': descrizioni, 'valutazioni': valutazioni, 'stagioni': stagioni}
        return render(request, 'gols/ricerca_gol.html', context)


def home(request):
    gol = Gol.objects.all()
    return render(request, 'gols/home.html',{'gol': gol})

