from django.shortcuts import render,get_object_or_404
from .models import Compilation
from gols.models import Gol

# Create your views here.

def compilations_ricerca_gol(request):
    if request.method == 'POST':
        nomeGiocatore = request.POST.get('nomeGiocatore', '')
        squadra = request.POST.get('squadra', '')
        competizione = request.POST.get('competizione', '')
        giornata = request.POST.get('giornata', '')
        descrizioneGoal = request.POST.get('descrizioneGoal', '')
        valutazione = request.POST.get('valutazione', '')
        stagione = request.POST.get('stagione', '')
        dataFrom = request.POST.get('dataFrom', '')
        dataTo = request.POST.get('dataTo', '')

        if(dataFrom=='' or dataTo==''):
            goal = Gol.objects.filter(
                nomeGiocatore__icontains=nomeGiocatore,
                squadra__icontains=squadra,
                competizione__icontains=competizione,
                giornata__icontains=giornata,
                descrizioneGoal__icontains=descrizioneGoal,
                valutazione__icontains=valutazione,
                stagione__icontains=stagione,
            ).order_by('data', 'ora', 'minutoGoal')
        else:
            goal = Gol.objects.filter(
                nomeGiocatore__icontains=nomeGiocatore,
                squadra__icontains=squadra,
                competizione__icontains=competizione,
                giornata__icontains=giornata,
                descrizioneGoal__icontains=descrizioneGoal,
                valutazione__icontains=valutazione,
                stagione__icontains=stagione,
                data__range=[dataFrom, dataTo]
            ).order_by('data', 'ora', 'minutoGoal')

        for goal1 in goal:
            goal1.video += "&mute=1"
            goal1.save()

        context = {'goal': goal, 'nomeGiocatore': nomeGiocatore, 'squadra': squadra, 'competizione': competizione,
                   'giornata': giornata, 'descrizioneGoal': descrizioneGoal, 'valutazione': valutazione,
                   'stagione': stagione}
        return render(request, 'gols/visualizza_gol.html', context)
    else:
        compilations = Compilation.objects.all().order_by('-dataFrom')
        return render(request, 'gols/home.html', {'compilations': compilations})


def compilation_detail(request, pk):
    if request.method == 'POST':
        nomeGiocatore = request.POST.get('nomeGiocatore', '')
        squadra = request.POST.get('squadra', '')
        competizione = request.POST.get('competizione', '')
        giornata = request.POST.get('giornata', '')
        descrizioneGoal = request.POST.get('descrizioneGoal', '')
        valutazione = request.POST.get('valutazione', '')
        stagione = request.POST.get('stagione', '')
        dataFrom = request.POST.get('dataFrom', '')
        dataTo = request.POST.get('dataTo', '')

        if(dataFrom=='' or dataTo==''):
            goal = Gol.objects.filter(
                nomeGiocatore__icontains=nomeGiocatore,
                squadra__icontains=squadra,
                competizione__icontains=competizione,
                giornata__icontains=giornata,
                descrizioneGoal__icontains=descrizioneGoal,
                valutazione__icontains=valutazione,
                stagione__icontains=stagione,
            ).order_by('data', 'ora', 'minutoGoal')
        else:
            goal = Gol.objects.filter(
                nomeGiocatore__icontains=nomeGiocatore,
                squadra__icontains=squadra,
                competizione__icontains=competizione,
                giornata__icontains=giornata,
                descrizioneGoal__icontains=descrizioneGoal,
                valutazione__icontains=valutazione,
                stagione__icontains=stagione,
                data__range=[dataFrom, dataTo]
            ).order_by('data', 'ora', 'minutoGoal')

        for goal1 in goal:
            goal1.video += "&mute=1&autoplay=1"
            goal1.save()

        context = {'goal': goal, 'nomeGiocatore': nomeGiocatore, 'squadra': squadra, 'competizione': competizione,
                   'giornata': giornata, 'descrizioneGoal': descrizioneGoal, 'valutazione': valutazione,
                   'stagione': stagione}
        return render(request, 'gols/visualizza_gol.html', context)
    else:
        compilation = get_object_or_404(Compilation, pk=pk)
        return render(request, 'compilations/compilation_detail.html', {'compilation': compilation})