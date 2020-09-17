from django import forms
from .models import Feed, RSVP

from django.core.exceptions import ValidationError

class RSVPForm(forms.Form):
    sender = forms.CharField(
            label = '이름',
            max_length = 60,
            )
    email = forms.CharField(
            label = '이메일',
            max_length = 120,
            )
    phone = forms.CharField(
            label = '휴대폰 번호',
            max_length=120,
            )

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if "@" and ".com" not in cleaned_data:
            raise ValidationError("유효한 이메일을 입력해주세요.")
        return cleaned_data

    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if "010" not in cleaned_data:
            raise ValidationError("유효한 휴대폰 번호를 입력해주세요.")
        return cleaned_data

