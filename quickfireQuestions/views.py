from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from user_profile.models import UserProfile
from monitorias.models import AffiliateCompany
# Create your views here.

@login_required
def questions_list(request):
    questionsList = Question.objects.all()
    return render(request, 'quickfireQuestions/questions_list.html', {'questionsList': questionsList})

@login_required
def questions_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'quickfireQuestions/questions_detail.html', {'question': question})

@login_required
def questions_new(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            userprofile = UserProfile.objects.get(pk=request.user.pk)
            userprofile.quickfirequestions_available -= 1
            userprofile.save()
            return redirect('quickfireQuestions:questions_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'quickfireQuestions/question_edit.html', {'form': form})

@login_required
def questions_edit(request,pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('quickfireQuestions:questions_detail', pk=post.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'quickfireQuestions/question_edit.html', {'form': form})


@login_required
def add_comment_to_questions(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.author = request.user
            comment.save()
            return redirect('quickfireQuestions:questions_detail', pk=question.pk)
    else:
        form = CommentForm()
    return render(request, 'quickfireQuestions/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('quickfireQuestions:questions_detail', pk=comment.question.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    question_pk = comment.question.pk
    comment.delete()
    return redirect('quickfireQuestions:questions_detail', pk=question_pk)


@login_required
def comment_correct_answer(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.isCorrectAnswer = True
    question_pk = comment.question.pk
    question = Question.objects.get(pk=question_pk)
    question.isAnswered = True
    question.save()
    comment.save()
    return redirect('quickfireQuestions:questions_detail', pk=question_pk)

@login_required
def quickfire_pay(request, option):
    if option == "online":
        userprofile = UserProfile.objects.get(pk=request.user.pk)
        userprofile.quickfirequestions_available = 3
        userprofile.save()
        return render(request, 'quickfireQuestions/online_payment_page.html')
    else:
        affiliates_list = AffiliateCompany.objects.all()
        return render(request, 'quickfireQuestions/onsite_payment_page.html', {'affiliates_list': affiliates_list})

@login_required
def questions_pay_accepted(request):
    return render(request, 'quickfireQuestions/accepted.html')

@login_required
def questions_pay_cancelled(request):
    return render(request, 'quickfireQuestions/cancelled.html')
