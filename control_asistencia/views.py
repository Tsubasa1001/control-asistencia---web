from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Cliente
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
