from django.db import models

# Create your models here.

class Table(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Activity(models.Model):
    DAYS =[
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
    ]
    TIME = [
        ('6:00', '6:00'), ('6:30', '6:30'),
        ('7:00', '7:00'), ('7:30', '7:30'),
        ('8:00', '8:00'), ('8:30', '8:30'),
        ('9:00', '9:00'), ('9:30', '9:30'),
        ('10:00', '10:00'), ('10:30', '10:30'),
        ('11:00', '11:00'), ('11:30', '11:30'),
        ('12:00', '12:00'), ('12:30', '12:30'),
        ('13:00', '13:00'), ('13:30', '13:30'),
        ('14:00', '14:00'), ('14:30', '14:30'),
        ('15:00', '15:00'), ('15:30', '15:30'),
        ('16:00', '16:00'), ('16:30', '16:30'),
        ('17:00', '17:00'), ('17:30', '17:30'),
        ('18:00', '18:00'), ('18:30', '18:30'),
        ('19:00', '19:00'), ('19:30', '19:30'),
        ('20:00', '20:00'), ('20:30', '20:30'),
        ('21:00', '21:00'), ('21:30', '21:30'),
        ('22:00', '22:00'),
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    day = models.CharField(max_length=9, choices=DAYS)
    time = models.CharField(max_length=5, choices=TIME)

    def __str__(self):
        return self.text