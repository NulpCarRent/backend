from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=150, default='Unknown', null=True)
    citizenship = models.CharField(max_length=50, default='Unknown', null=True)
    repeated_client = models.BooleanField(default=False, null=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("Client_detail", kwargs={"pk": self.pk})

class Auto(models.Model):

    name = models.CharField(max_length=100, default='Unknown', null=True)
    renter = models.ForeignKey(Client, models.CASCADE, related_name='auto_renters', default=None, null=True)
    release_year = models.IntegerField(default=2000, null=True)
    price = models.IntegerField(default=0, null=True)

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Auto_detail", kwargs={"pk": self.pk})

class Request(models.Model):

    renter = models.ForeignKey(Client, models.CASCADE, related_name='request_renters', default=None, null=True)
    auto = models.ForeignKey(Auto, models.CASCADE, related_name='request_autos', default=None, null=True)
    rent_date = models.DateField(default=None, null=True)
    due_date = models.DateField(default=None, null=True)


    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"

    def __str__(self):
        return self.auto.name

    def get_absolute_url(self):
        return reverse("Request_detail", kwargs={"pk": self.pk})