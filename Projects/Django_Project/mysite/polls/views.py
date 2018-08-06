from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
#from django.template import loader
# Create your views here.
from .models import Question

def my(request):

    return render(request,'polls/my.html')

def detail(request,question_id):
    return render(request,'polls/detail.html'),#{'question':question})

# return HttpResponse("You're lokking at question %s."%question_id)
""" try:
        question = Question.objects.get(pk=question_id)
     except Question.DoesNotExist:

        raise Http404("Question does not exist")
     return render(request,'polls/detail.html',{'question':question})
"""
#question = get_object_or_404(Question,pk=question_id)



def results(request,question_id):

    response = "You're looking at the results of question %s."
    return HttpResponse(response%question_id)


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = { 'latest_question_list':latest_question_list,}
  #  return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def vote(request,question_id):

    """question = get_object_or_404(Question,pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,choice.DoesNotExist):
        return redner(request,'polls/detail.html',{'question':question,'error_message':"You did'nt select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reversed('polls:results',args=(question.id,)))
"""
    return  HttpResponse("You're voting on question %s."%question_id)
