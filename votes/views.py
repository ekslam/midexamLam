from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Position, Vote
from .forms import CandidateModelForm, PositionModelForm
from datetime import datetime
# Create your views here.

def index(request):
    cands = {}
    candidate = Candidate.objects.all()
    #vote = Vote.objects.all()
    cands['candidate'] = candidate
    #cands['vote'] = vote
    return render(request,'index.html',cands)


def candidate_detail(request, votes_id):
    cands = {}
    cands['candidate'] = Candidate.objects.get(id=votes_id)
    return render(request, 'detail.html', content)


def candidate_create(request):
    cands = {}
    cands['form'] = CandidateModelForm()
    if request.method == 'POST':
        form = CandidateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/votes/')
        else:
            cands['form'] = form
            render(request, 'create.html', cands)
    else:
        return render(request, 'create.html', cands)


def candidate_update(request):
    cands = {}
    candidate = Candidate.objects.get(id=votes_id)
    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate updated')
        else:
            cands['form'] = form
            render(request, 'update.html', cands)
    else:
        #question = Question.objects.get(id=question_id)
        cands['form'] = PostModelForm(instance=candidate)
        #context['q_id'] = question_id
    return render(request, 'update.html', cands)


def position_create(request):
    pos = {}
    pos['form'] = PositionModelForm()
    if request.method == 'POST':
        form = PositionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/votes/')
        else:
            pos['form'] = form
            render(request, 'position.html', pos)
    else:
        return render(request, 'position.html', pos)

def vote(request, votes_id):
    cands = Candidate.objects.get(id=candidate_id)
    cands.vote.all().count()
