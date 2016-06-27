from django.shortcuts import render
from .models import Question
# Create your views here.

def questions_list(request):
    questionsList = Question.objects.all()
    return render(request, 'quickfireQuestions/questions_list.html', {'questionsList': questionsList})


