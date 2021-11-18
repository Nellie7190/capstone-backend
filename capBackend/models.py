from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField( max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.userName
   

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    isBlackOwned = models.BooleanField()
    isWomanOwned = models.BooleanField()
    isENMOwned = models.BooleanField()
    isLComOwned = models.BooleanField()
    allowsPets = models.BooleanField()
    # change the field type
    hoursOpen = models.CharField(max_length=10, default='0')

    def __str__(self):
        return self.name

class Review(models.Model):
    # figure out how to add Review to be owned by BOTH User & Place
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    isBlackOwned = models.BooleanField(default=False)
    isWomanOwned = models.BooleanField(default=False)
    isENMOwned = models.BooleanField(default=False)
    isLComOwned = models.BooleanField(default=False)
    allowsPets = models.BooleanField(default=False)
    # change the field type
    hoursOpen = models.CharField(default='0', max_length=10)
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=200, default='no reviews')

    def __str__(self):
        return self.comment
