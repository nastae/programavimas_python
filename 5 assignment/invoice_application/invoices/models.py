from django.db import models
from django.urls import reverse
from login.models import User

class Form(models.Model):
    company = models.CharField(max_length=50)
    order_approval_number = models.IntegerField()
    established_at = models.DateTimeField()
    approved_at = models.DateTimeField()
    commisioner_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner1', blank=False, null=True)
    commisioner_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner2', blank=True, null=True)
    commisioner_3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner3', blank=True, null=True)
    commisioner_4 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commissioner4', blank=True, null=True)
    purchase_doc_seller = models.CharField(max_length=50)
    purchase_doc_number = models.IntegerField()
    purchase_doc_serial = models.CharField(max_length=50)
    purchase_doc_at = models.DateTimeField()
    responsible_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible_user', blank=False, null=True)

    def get_absolute_url(self):
        return reverse('form-list')

class Invoice(models.Model):
    name = models.CharField(max_length=50)
    VNT = 'VNT'
    KOMPL = 'KOMPL'
    measurement_type = (
        (VNT, 'vnt.'),
        (KOMPL, 'kompl.'),
    )
    measurement = models.CharField(
        max_length=10,
        choices=measurement_type,
        default=VNT,
    )
    amount = models.IntegerField()
    sum = models.FloatField()
    cost = models.FloatField()
    location = models.CharField(max_length=50)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('invoice-create')
