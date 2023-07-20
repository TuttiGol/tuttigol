from django.db import models



# Create your models here.

class Compilation(models.Model):

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
        ('2009/2010', '2009/2010'),
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
        ('Coast to coast', 'Coast to coast'),
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
    image = models.ImageField()
    titoloCompilation = models.CharField(max_length=1000, null=False)
    descrizioneCompilation = models.TextField()
    nomeGiocatore = models.CharField(max_length=100, blank=True)
    squadra = models.CharField(max_length=100, blank=True)
    giornata = models.CharField(max_length=100, blank=True)
    competizione = models.CharField(max_length=100, choices=COMPETIZIONI_PREDEFINITI,blank=True)
    descrizioneGoal = models.CharField(max_length=500, choices=GOAL_PREDEFINITI,blank=True)
    stagione = models.CharField(max_length=100, choices=STAGIONI_PREDEFINITE,blank=True)
    valutazione = models.CharField(max_length=100, choices=VALUTAZIONE_PREDEFINITI,blank=True)
    dataFrom = models.CharField(max_length=100,blank=True)
    dataTo = models.CharField(max_length=100,blank=True)

    class Meta:
        unique_together = ['titoloCompilation']

    def __str__(self):
        return self.titoloCompilation
