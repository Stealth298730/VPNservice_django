from django import forms

from .models import Subscription


class Subform(forms.ModelForm):
    sub = forms.ChoiceField(
        choices = Subscription,
        label="Виберіть підписку",
        attrs=forms.RadioSelect(attrs={})
        )