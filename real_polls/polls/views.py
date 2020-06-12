from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Poll
from django.urls import reverse
from .forms import AddPollForm

from django.forms import ModelForm 

# Create your views here.

def index(request):
	polls = Poll.objects.all()
	context = {
		'polls': polls,
	}
	return render(request, 'polls/index.html', context)

#Show specific question and choices

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question doesn't exist")
	return render(request, 'polls/detail.html', {'question':question})

#Get Question and display result

def results(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)
	context = {
		'poll': poll
	}
	return render(request, 'polls/results.html', context)


#vote for a question choice 

def vote(request, poll_id): 
	poll = Poll.objects.get(pk=poll_id)

	if request.method == 'POST':
		selected_option = request.POST['poll']
		if selected_option == 'option1':
			poll.option_one_count += 1
		elif selected_option == 'option2':
			poll.option_two_count += 1
		elif selected_option == 'option3':
			poll.option_three_count += 1
		else: 
			return HttpResponse(400, "Invalid Form")
		poll.save()
		return redirect('polls:results', poll.id)
	context = {
		'poll':poll
	}
	return render(request, 'polls/vote.html', context)


#Adding a new poll

def add_poll(request):
	if request.method == 'POST':
		form = AddPollForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('polls:index')
	else:
		form = AddPollForm()
	context = {
		'form':form
	}
	return render(request, 'polls/add.html', context)
