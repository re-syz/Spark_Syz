"""
131072
280918
CS+X
"""






# =============

from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random



# =============

def index(request):
    Kort = str("Kort")
    Spark = str("Spark")
    return render(request, 'index.html')
