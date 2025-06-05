from django import forms

from ..models.apupo import Apupo

MAX_APUPO_LENGHT = 140


class ApupoForm(forms.ModelForm):
    class Meta:
        model = Apupo
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_APUPO_LENGHT:
            raise forms.ValidationError("This apupo is too long")
        return content
