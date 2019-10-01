from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import secrets


class DateMixin(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    complete = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NWA(models.Model):
    nwa = models.CharField(max_length=20)

    def __str__(self):
        return self.nwa

    class Meta:
        verbose_name = 'NWA'
        verbose_name_plural = 'NWAs'


class SerialNumber(models.Model):
    serial_number = models.CharField(max_length=100)

    def __str__(self):
        return self.serial_number


class Component(models.Model):
    name = models.CharField(max_length=200)
    part_number = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class ArmoryComponent(models.Model):
    armory = models.ForeignKey('Armory', on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    qty = models.IntegerField()

    def __str__(self):
        return self.component.name


class Armory(models.Model):
    quote = models.ForeignKey('Quote', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
    user_manual = models.FileField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        price = 0
        for component in ArmoryComponent.objects.filter(armory=self.pk):
            print(component.component.price)
            print(component.qty)
            price += component.component.price * component.qty
        self.price = price
        super().save(*args, **kwargs)

    def __str__(self):
        return '$' + str(self.price)


class POC(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    commercial = models.EmailField(max_length=100)
    dsn = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField(max_length=1000)


class Note(models.Model):
    note = models.FileField()

    def __str__(self):
        return self.note.name


class Image(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class Quote(DateMixin):
    quote_number = models.CharField(max_length=100, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    nwa = models.ManyToManyField(NWA, blank=True)
    serial_number = models.ManyToManyField(SerialNumber, blank=True)
    user = models.ManyToManyField(User, blank=True)
    poc = models.ForeignKey(POC, on_delete=models.SET_NULL, null=True, blank=True)
    size_width = models.FloatField(null=True, blank=True)
    size_depth = models.FloatField(null=True, blank=True)
    size_height = models.FloatField(null=True, blank=True)
    comment = models.ManyToManyField(Comment, blank=True)
    note = models.ManyToManyField(Note, blank=True)
    image = models.ManyToManyField(Image, blank=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.quote_number = timezone.now().strftime("GN-%y%m%d%H%M%S-") + secrets.token_urlsafe(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.quote_number
