from django import forms
from .models import Post,  Order, Product #,Comment 

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
            max_value = 3,
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


    def clean(self):
        cleaned_data = super().clean()
        sender = cleaned_data.get('sender')
        author = cleaned_data.get('author')
        quantity = cleaned_data.get('quantity')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        message_store = cleaned_data.get('message_store')
        signature = cleaned_data.get('signature')


#class OrderForm(forms.Form):
#   author = forms.CharField(
#            max_length=60,
#            widget=forms.TextInput(attrs={
#                "class": "form-control",
#                "placeholder": " 이름 또는 닉네임을 적어주세요!"
#                })
#            )
#    quantity  = forms.IntegerField(
#            widget=forms.Textarea(attrs={
#                "class": "form-control",
#                "placeholder": "주문 수량(1회 주문 최대 10장) "
#                 })
#             )
#    phone = forms.CharField(
#            widget=forms.Textarea(attrs={
#                "class": "form-control",
#                "placeholder": "휴대폰 번호: 양식 010-OOOO-OOOO "
#                })
#            )
#    message_store  = forms.CharField(
#            widget=forms.Textarea(attrs={
#                "class": "form-control",
#                "placeholder": "사장님께 보내는 한마디(전체공개) "
#                })
#            )

#class CommentForm(forms.Form):
#    author = forms.CharField(
#            max_length=60,
#            widget=forms.TextInput(attrs={
#                "class": "form-control",
#                "placeholder": "Your Name | 이름을 적어주세요!"
#                })
#            )
#    body = forms.CharField(widget=forms.Textarea(attrs={
#            "class": "form-control",
#            "placeholder": "Leave a comment! | 댓글을 남겨주세요! "
#            })
#        )

