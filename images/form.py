from http.client import responses
from tkinter import image_names

import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib3 import request

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','url','description']
        widgets = {
            'url': forms.HiddenInput,
        }


def clean_url(self):
    url = self.cleaned_data['url']
    valid_extensions = ['jpg','jpeg','png']
    extension = url.rsplit('.',1)[1].lower()
    if extension not in valid_extensions:
        raise forms.ValidationError("Podany url nie zawiera poprawnego rozszerzenia ")
    return url

def save(self, force_insert = False, force_update = False, commit=True):
    image = super().save(commit=False)
    image_url = self.cleaned_data['url']
    extension =  image_url.split('.',1)[1].lower()
    name = slugify(image.title)
    image_name = f'{name}.{extension}'


    response = requests.get(image_url)
    image.image.save(image_name,ContentFile(response.content),save=False)

    if commit:
        image.save()

    return image