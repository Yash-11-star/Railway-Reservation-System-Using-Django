from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Trains(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    train_name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    price=models.FloatField(default=120)
    seats_available=models.IntegerField()

# Using a post-save signal to synchronize data between TrainAdmin and Reservation apps
@receiver(post_save, sender=Trains)
def create_or_update_reservation_train(sender, instance, created, **kwargs):
    from reservation.models import trains as ReservationTrain
    
    if created:
        ReservationTrain.objects.create(
            train_name=instance.train_name,
            source=instance.source,
            destination=instance.destination,
            time=instance.time,
            price=instance.price,
            seats_available=instance.seats_available
            
        )
    else:
        reservation_train = ReservationTrain.objects.get(id=instance.id)
        reservation_train.train_name = instance.train_name
        reservation_train.source = instance.source
        reservation_train.destination = instance.destination
        reservation_train.time = instance.time
        reservation_train.price = instance.price
        reservation_train.seats_available = instance.seats_available
        reservation_train.save()
