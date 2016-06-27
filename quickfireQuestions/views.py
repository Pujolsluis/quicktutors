from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.


def questions_list(request):
    questionsList = Question.objects.all()
    return render(request, 'quickfireQuestions/questions_list.html', {'questionsList': questionsList})


def questions_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'quickfireQuestions/questions_detail.html', {'question': question})


