from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

User = get_user_model()

# Create your models here.
# trips & notes (images)
class Trip(models.Model):
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=2)
  start_date = models.DateField(blank=True, null=True)
  end_date = models.DateField(blank=True, null=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
  # Django comes pre built with user authentication tools.

  def __str__(self):
    return self.city
  
# each note is associated with a trip
class Note(models.Model):
  EXCURSIONS = (
    ("event", "Event"),
    ("dining", "Dining"),
    ("experience", "Experience"),
    ("general", "General"),
  )

  trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
  name = models.CharField(max_length=100)
  description = models.TextField()
  type = models.CharField(max_length=100, choices=EXCURSIONS)
  img = models.ImageField(upload_to='notes', blank=True, null=True)
  # Python uses Pillow package to process images.
  rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])
  # Validators can be imported from Django, a built in foundation.

  def __str__(self):
    return f"{self.name} in {self.trip.city}"