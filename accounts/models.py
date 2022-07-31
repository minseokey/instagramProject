from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import RegexValidator
from django.template.loader import render_to_string

# 기본 장고의 회원가입 방법 사용
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M" , "Male"
        FEMALE = "F" , "Female"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length =13,blank=True,validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length =1,blank=True,choices=GenderChoices.choices)
    avatar = models.ImageField(blank=True , upload_to="accounts/avatar/%Y/%m/%d",
                            help_text = "48 * 48 크기의 jpg,png 파일을 업로드해주세요")
    # def send_welcome_email(self):

    #     subject = render_to_string("accounts\templates\accounts\welcome_email_subject.txt",{"user" : self})
    #     content = render_to_string("accounts\templates\accounts\welcome_email_content.txt",{"user" : self})

    #     sender_email = "settings.WELCOME_EMAIL_SENDER"

    #     send_mail(subject,content,sender_email,[self.email],fail_silently=False)
    #     #TODO sendgrid 설정. api키가 안나와요...
