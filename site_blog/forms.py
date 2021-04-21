from django import forms
from django.core import validators


class CommentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "لطفا نام خود را وارد کنید *", "class": "form-control",
                   "oninvalid": "setCustomValidity('فیلد را پر کنید')"}),
        label="نام", required=True,
        validators=[validators.MaxLengthValidator(100, "نام و نام خانوادگی شما نمی تواند بیشتر از 100 کارکتر باشد"), ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": " * لطفا ایمیل خود را وارد کنید", "class": "form-control",
                                       "oninvalid": "setCustomValidity('فیلد را پر کنید یا ایمیل را درست وارد کنید')"}),
        label="ایمیل", required=True,
        validators=[validators.EmailValidator("ایمیل وارد شده نادرست است")]
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "لطفا متن نظر خود را وارد کنید *", "class": "form-control textarea", "rows": "4",
                   "id": "commentForm",
                   "tabindex": "tabindex",
                   "oninvalid": "setCustomValidity('فیلد را پر کنید')"}),
        label="متن نظر", required=True
    )

