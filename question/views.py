from django.shortcuts import render
from question.models import MathQues, AllQues
from django.utils.timezone import now
from django.contrib import messages

# Create your views here.

def mathCount():
    allMathQues = MathQues.objects.all()
    count = allMathQues.count()
    print(count)
    return count+1