from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  realtor       = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title         = models.CharField(max_length=200)
  description   = models.TextField(blank=True)
  address       = models.CharField(max_length=100)
  city          = models.CharField(max_length=100)  # models.ForeignKey(City, on_delete=models.DO_NOTHING)
  state         = models.CharField(max_length=100)  # models.ForeignKey(State, on_delete=models.DO_NOTHING)
  zipcode       = models.CharField(max_length=20)
  price         = models.IntegerField()
  bedrooms      = models.IntegerField()
  bathrooms     = models.DecimalField(max_digits=2, decimal_places=1)
  square_feet   = models.DecimalField(max_digits=7, decimal_places=2)
  lot_size      = models.DecimalField(max_digits=7, decimal_places=2)
  is_published  = models.BooleanField(default=True)
  garage        = models.IntegerField(default=0)
  listing_date  = models.DateTimeField(default=datetime.now, blank=True)
  main_photo    = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

  def __str__(self):
    return self.title