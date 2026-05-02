from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey('ItemList', related_name="items", on_delete=models.CASCADE)
    Image = CloudinaryField('image', blank=True, null=True)  # ← changed

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

    def __str__(self):
        return self.Description

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = CloudinaryField('image', blank=True, null=True)  # ← changed

    def __str__(self):
        return self.User_name

class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
