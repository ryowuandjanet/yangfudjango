import django_filters
from .models import * 

class YfcaseFilter(django_filters.FilterSet):

  class Meta:
    model = Yfcase
    fields = ['yfcaseCaseNumber', 'yfcaseCity']