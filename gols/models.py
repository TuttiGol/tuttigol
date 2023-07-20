from django.db import models
import datetime

# Create your models here.

class Gol(models.Model):
    ORARI_PREDEFINITI = [
        (datetime.time(10, 0), '10:00'),
        (datetime.time(11, 0), '11:00'),
        (datetime.time(12, 0), '12:00'),
        (datetime.time(12, 30), '12:30'),
        (datetime.time(13, 0), '13:00'),
        (datetime.time(14, 0), '14:00'),
        (datetime.time(15, 0), '15:00'),
        (datetime.time(16, 0), '16:00'),
        (datetime.time(17, 0), '17:00'),
        (datetime.time(18, 0), '18:00'),
        (datetime.time(18, 30), '18:30'),
        (datetime.time(19, 0), '19:00'),
        (datetime.time(20, 0), '20:00'),
        (datetime.time(21, 0), '21:00'),
    ]

    COMPETIZIONI_PREDEFINITI = [
        ('Serie A', 'Serie A'),
        ('Serie B', 'Serie B'),
        ('Champions League', 'Champions League'),
        ('Mondiali 2006', 'Mondiali 2006'),
        ('Coppa Italia', 'Coppa Italia'),
        ('Eredivise', 'Eredivise'),
        ('Europa League', 'Europa League'),
    ]

    STAGIONI_PREDEFINITE = [
        ('2022/2023', '2022/2023'),
        ('2021/2022', '2021/2022'),
        ('2006/2007', '2006/2007'),
        ('2001/2002', '2001/2002'),

    ]

    GOAL_PREDEFINITI = [
        ('Testa', 'Testa'),
        ('Rigore', 'Rigore'),
        ('Al volo', 'Al volo'),
        ('GDM', 'GDM'),
        ('Tiro da fuori', 'Tiro da fuori'),
        ('Tiro in area', 'Tiro in area'),
        ('Punizione', 'Punizione'),
        ('Dribling sul portiere', 'Dribling sul portiere'),
        ('Pallonetto', 'Pallonetto'),
        ('Autogol', 'Autogol'),
        ('Coast to coast','Coast to coast'),
        ('Rovesciata', 'Rovesciata'),
        ('Mezza Rovesciata', 'Mezza Rovesciata'),
    ]

    VALUTAZIONE_PREDEFINITI = [
        ('1 stella', '1 stella'),
        ('2 stelle', '2 stelle'),
        ('3 stelle', '3 stelle'),
        ('4 stelle', '4 stelle'),
        ('5 stelle', '5 stelle'),
    ]

    video = models.CharField(max_length=5000, null=False)
    nomeGiocatore = models.CharField(max_length=100, null=False)
    squadra = models.CharField(max_length=100, null=False)
    partita = models.CharField(max_length=100, null=False)
    giornata = models.CharField(max_length=100, null=False)
    ora = models.TimeField(choices=ORARI_PREDEFINITI, default=datetime.time(12, 0))
    competizione = models.CharField(max_length=100, choices=COMPETIZIONI_PREDEFINITI)
    descrizioneGoal = models.CharField(max_length=500, choices=GOAL_PREDEFINITI)
    minutoGoal = models.IntegerField(null=False, default=1)
    stagione = models.CharField(max_length=100, choices=STAGIONI_PREDEFINITE)
    valutazione = models.CharField(max_length=100, choices=VALUTAZIONE_PREDEFINITI)
    data = models.CharField(max_length=100, default='0000-00-00')

    class Meta:
        unique_together = ['partita', 'data']

    def __str__(self):
        return self.nomeGiocatore