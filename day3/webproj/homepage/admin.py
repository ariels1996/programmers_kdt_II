from django.contrib import admin
from .models import Coffee, Chicken

# Register your models here.
# 어드민으로 모델을 관리할 수 있음
admin.site.register(Coffee)
admin.site.register(Chicken)
