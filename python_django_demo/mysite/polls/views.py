from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
# Create your views here.

def index(request):
    # return HttpResponse("Hello, wold. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # ①
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list
    # }
    # return HttpResponse(template.render(context, request))
    # ②
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # response = "You're looking at question %s."
    # return HttpResponse(response % question_id)
    # ① 404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # context = {
    #     'question' : question
    # }
    # return render(request, 'polls/detail.html', context)
    # ② 404
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question" : question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    # respone = "You're voting on question %s."
    # return HttpResponse(respone % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
