from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    result = []
    for question in latest_question_list:
	result.append("/static/" + question.image.url)
    template = loader.get_template('votes/index.html')
    context = RequestContext(request, {
        'result': result,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
