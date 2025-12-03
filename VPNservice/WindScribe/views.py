from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from .models import Subscription,Service

# Create your views here.

def get_sub_view(request:HttpRequest):
    pass