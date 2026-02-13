from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver # receiver é um decorador que serve para registrar a função como um receptor de sinais, ou seja, ela será chamada quando o sinal for emitido
from bikes.models import Bike

@receiver(pre_save, sender=Bike)
def bike_pre_save(sender, instance, **kwargs): # sender serve para identificar qual modelo está sendo salvo, instance é a instância do modelo que está sendo salva e **kwargs serve para receber outros argumentos que possam ser passados
    print(' PRE SAVE ')


@receiver(post_save, sender=Bike)
def bike_post_save(sender, instance, **kwargs):
    print(' POST SAVE ')


@receiver(pre_delete, sender=Bike)
def bike_pre_delete(sender, instance, **kwargs):
    print(' PRE DELETE ')


@receiver(post_delete, sender=Bike)
def bike_post_delete(sender, instance, **kwargs):
    print(' POST DELETE ')