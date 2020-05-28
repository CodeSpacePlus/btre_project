import os
from faker import Factory
from datetime import datetime
from listings.models import Listing
from realtors.models import Realtor

fake = Factory.create()

def create(realtors=1, listings=3):
  print("Creating new realtors with it's listings")
  for _ in range(realtors):
    test_realtor = Realtor.objects.create(name=fake.name(),
                                          description=fake.text(),
                                          email=fake.email(),
                                          phone=fake.phone_number(),
                                          is_mvp=False)

    for _ in range(listings):
      myaddress = fake.street_address()
      Listing.objects.create(realtor=test_realtor,
                              title=myaddress,
                              description=fake.text(),
                              address=myaddress,
                              city=fake.city(),
                              state=fake.state(),
                              zipcode=fake.zipcode(),
                              price=fake.random_number(),
                              bedrooms=fake.random_int(min=0, max=15),
                              bathrooms=fake.random_int(min=0, max=9),
                              square_feet=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                              lot_size=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
                              is_published=fake.boolean(),
                              garage=fake.random_int(min=0, max=3))