from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class SubscriptionForm(forms.ModelForm):
    """SubscriptionForm"""
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class' : 'footer__email-input', 'placeholder':_("Введите ваш email"), 'maxlength':100}))
    class Meta:
        model = Email
        fields = ("email",)

class Subscription2Form(forms.ModelForm):
    """Subscription2Form"""
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class' : 'email-input', 'placeholder':_("Введите ваш email"), 'maxlength':100}))
    class Meta:
        model = Email
        fields = ("email",)

class ContactForm(forms.ModelForm):
    """SubscriptionForm"""
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'contact__form-input', 'placeholder':_("ФИО"), 'maxlength':254}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class' : 'contact__form-input', 'placeholder':"Email", 'maxlength':100}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'contact__form-input', 'placeholder':_("Телефон"), 'maxlength':15}))
    company = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'contact__form-input', 'placeholder':_("Компания"), 'maxlength':100}))
    message =forms.CharField(label='', widget=forms.Textarea(attrs={'class' : 'contact__form-input', 'placeholder':_("Сообщение"), 'maxlength':450}))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'company', 'message')

class AddBlogForm(forms.ModelForm):
    """AddBlogForm"""
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'contact__form-input', 'placeholder':"Название статьи", 'maxlength':113}))
    main_text = forms.CharField(label='', widget=forms.Textarea(attrs={'class' : 'contact__form-input', 'placeholder':"Основной текст, чтобы перейти на след. обзац используй в тексте <br><br>"}))
    class Meta:
        model = Blog
        fields = ('name', 'main_text')
