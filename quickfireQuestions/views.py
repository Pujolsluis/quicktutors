from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm
from django.utils import timezone
# Create your views here.


def questions_list(request):
    questionsList = Question.objects.all()
    return render(request, 'quickfireQuestions/questions_list.html', {'questionsList': questionsList})


def questions_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'quickfireQuestions/questions_detail.html', {'question': question})

def questions_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return redirect('quickfireQuestions:questions_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'quickfireQuestions/question_edit.html', {'form': form})
