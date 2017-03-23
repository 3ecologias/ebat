# -*- coding: UTF-8 -*-
from django import forms
from django.core.mail import EmailMessage, BadHeaderError

class Call_me(forms.Form):
    phone = forms.CharField(required=True,label='', widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'(XX) XXXXX XXXX', 'aria-describedby':'basic-addon2', 'type':'tel'}))

    def send_email(self):
        phone = self.cleaned_data['phone']
        subject = 'ME LIGUE!'

        try:
            email = EmailMessage(subject+" ,Telefone "+phone, phone, 'ebat.atendimento@gmail.com',['ebat.atendimento@gmail.com'])
            email.content_subtype = "html"
            email.send()

        except BadHeaderError:
            raise ValidationError("Cabeçalho inválido")
