from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    
    #...

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})
    return HttpResponse('You are looking at question %s.' % question_id)

def results(request, question_id):
    response = 'You are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)