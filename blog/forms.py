from django import forms
from .models import Post,  Order, Product #,Comment 

from django.core.exceptions import ValidationError

class OrderForm(forms.Form):
    sender  = forms.CharField(
            label = '이름',
            max_length =60,
            widget=forms.TextInput(attrs={"placeholder": "결제시 입금자명"}),
            )
    author  = forms.CharField(
            label = '닉네임',
            max_length =60,
            widget=forms.TextInput(attrs={"placeholder": "하단 댓글창에 표시 "})
            )
    quantity  = forms.IntegerField(
            label = '쿠폰 수량',
            #max_value = 3,
            widget=forms.TextInput(attrs={"placeholder": "숫자만 입력 |  1회 주문 최대 3장"})
            )
    email = forms.CharField(
            label = '이메일',
            widget=forms.TextInput(attrs={'placeholder': '주문확인, 결제안내 및 쿠폰수신'})
            )
    phone = forms.CharField(
            label = '휴대폰 번호',
            max_length=120,
            widget=forms.TextInput(attrs={'placeholder': '결제안내 문자 수신'})
            )
    message_store = forms.CharField(
            label = '사장님께 보내는 한 마디! ',
            max_length=256,
            widget=forms.TextInput(attrs={'placeholder': '게시글 하단 전체공개'})
            )
    signature = forms.CharField(
            label = '주문서를 제출하시기 전에 <필독사항>을 다시 한 번 확인 부탁드립니다.',
            max_length=120,
            widget=forms.TextInput(attrs={'placeholder': '주문과 결제에 동의하신다면, "네"를 입력해주세요.'})
            )

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if "@" and ".com" not in cleaned_data:
            raise ValidationError("유효한 이메일을 입력해주세요.")
        return cleaned_data

    def clean_quantity(self):
        cleaned_data = self.cleaned_data['quantity']
        if 4 <= cleaned_data:
            raise ValidationError("1회 최대 3장까지만 주문 가능합니다.")
        if cleaned_data != int:
            raise ValidationError("유효한 숫자를 입력해주세요.")
        return cleaned_data

    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if "010" not in cleaned_data:
            raise ValidationError("유효한 휴대폰 번호를 입력해주세요.")
        return cleaned_data

    def clean_signature(self):
        cleaned_data = self.cleaned_data['signature']
        if "네" not in cleaned_data:
            raise ValidationError("확인 후 제출 가능합니다.")
        return cleaned_data

    #def clean(self):
    #    cleaned_data = super().clean()
    #    sender = cleaned_data.get('sender')
    #    author = cleaned_data.get('author')
    #    quantity = cleaned_data.get('quantity')
    #    email = cleaned_data.get('email')
    #    phone = cleaned_data.get('phone')
    #    message_store = cleaned_data.get('message_store')
    #    signature = cleaned_data.get('signature')

    #quantity = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(3)])



