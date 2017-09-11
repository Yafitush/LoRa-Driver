from django.db import models
from django_countries.fields import CountryField
from django.core.urlresolvers import reverse



class Organization(models.Model):
    ORGANIZATIONS_TYPES = (
        ('SUPERMARKET', 'Supermarket'),
        ('FAST-FOOD', 'Fast-Food'),
        ('SMART-BUILDING', 'Smart Building'),
        ('CINEMA', 'Cinema'),
    )
    name = models.CharField(max_length=200)
    organization_type = models.CharField(max_length=20, choices=ORGANIZATIONS_TYPES, default='SUPERMARKET')
    country = CountryField(default="Israel")
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('organization:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + " " + self.organization_type
