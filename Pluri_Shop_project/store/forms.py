from django import forms

from .models import User_compt


class create_compteforms(forms.ModelForm):
    class Meta:
        model=User_compt
        fields=('__all__')
        widget={

        }