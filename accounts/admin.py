from django.contrib import admin
from .models import User

# 장고 어드민이 장고 폼을 사용하기때문에 웹사이트랑 바이오 나옴
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','website_url','is_active','is_superuser','is_staff']
  

