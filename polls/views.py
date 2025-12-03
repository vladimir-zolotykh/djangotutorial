from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render


def index(request):
    # http://localhost:8000/polls/
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # http://localhost:8000/polls/1/
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    # http://localhost:8000/polls/1/results/
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    # http://localhost:8000/polls/1/vote/
    return HttpResponse("You're voting on question %s." % question_id)
