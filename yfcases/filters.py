from django import forms
import django_filters
from .models import * 

FINALDECISION_CHOICES = [
  ("",""),
  ("未判定","未判定"),
  ("1拍進場","1拍進場"),
  ("2拍進場","2拍進場"),
  ("3拍進場","3拍進場"),
  ("4拍進場","4拍進場"),
  ("放棄","放棄")
]
# https://wreadit.com/@wwwlearncodewithmikecom/post/50118
class YfcaseFilter(django_filters.FilterSet):
  yfcaseCaseNumber = django_filters.CharFilter(
    label='案號',
    lookup_expr='icontains',
    widget=forms.TextInput(attrs={'class': 'form-control'})
  ) 
  yfcaseFinalDecision = django_filters.ModelChoiceFilter(label='最終判定',queryset=FinalDecision.objects.all())
  # yfcaseFinalDecision = django_filters.ChoiceFilter(
  #   label='最終判定',
  #   choices=FINALDECISION_CHOICES
  # )

  class Meta:
    model = Yfcase
    fields = ['yfcaseCaseNumber', 'yfcaseCity','user','yfcaseFinalDecision']