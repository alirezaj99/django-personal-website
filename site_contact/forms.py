from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "لطفا نام و نام خانوادگی خود را وارد کنید", "id": "nameContact",
                   "name": "nameContact", "autocomplete": "on", "class": "form-control",
                   "oninvalid": "setCustomValidity('فیلد را پر کنید')", "onkeyup": "setCustomValidity('')"}),
        required=True,
        label="نام و نام خانوادگی",
        validators=[validators.MaxLengthValidator(200, "نام و نام خانوادگی شما نمی تواند بیشتر از 200 کارکتر باشد")]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "لطفا ایمیل خود را وارد کنید", "id": "emailContact", "name": "emailContact",
                   "autocomplete": "on", "class": "form-control",
                   "oninvalid": "setCustomValidity('فیلد را پر کنید یا ایمیل را درست وارد کنید')",
                   "onkeyup": "setCustomValidity('')"}),
        required=True,
        label="ایمیل",
        validators=[validators.EmailValidator("ایمیل شما نادرست است")]
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "لطفا متن پیام خود را وارد کنید", "row": "4",
                   "id": "messageContact", "class": "form-control", "name": "messageContact",
                   "oninvalid": "setCustomValidity('فیلد را پر کنید')", "onkeyup": "setCustomValidity('')"}),
        required=True,
        label="متن پیام",
    )
