from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from forms import QuestionForm, ChoiceForm
from models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last five published questions."""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
def home(request):
    return render(request, 'base.html')

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render( request, "polls/details.html", {
            'question': p,
            'error_mensage': "You didn't select a choice.",
        } )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
# Create your views here.here

@login_required
def create_question(request):
    form = QuestionForm(request.POST or None)
    #choice_form = ChoiceForm(request.POST or None)
    if form.is_valid(): #and choice_form.is_valid():
        #choice = choice_form.save(commit=False)
        question = form.save(commit=False)
        question.pub_date = timezone.now()
        question.save()
        #choice.question = question
        #choice.save()
        return redirect(reverse("polls:index"))

    return render(request, 'polls/my_template.html', {'form':form,})# 'choice_form':choice_form})

def edit_question(request, question_id):
    a_question = get_object_or_404(Question, pk=question_id)
    form = QuestionForm (request.POST or None, instance = a_question)
    if form.is_valid():
        question = form.save()
        return redirect(reverse("polls:index"))

    return render (request, "polls/edit_template.html", {'form': form })

def delete_question(request, question_id):
    u = get_object_or_404(Question, pk=question_id).delete()
    return HttpResponseRedirect(reverse('polls:index'))

def create_choice(request, question_id):
    choice_form = ChoiceForm(request.POST or None)
    if choice_form.is_valid(): #and choice_form.is_valid():
        choice = choice_form.save(commit=False)
        choice.question = get_object_or_404(Question, pk=question_id)
        choice.save()
        return redirect(reverse("polls:detail", kwargs={'pk':question_id}))

    return render(request, 'polls/create_choice.html', {'choice_form':choice_form, 'question_id':question_id})

def edit_choice(request, question_id, choice_id):
    a_choice = get_object_or_404(Choice, pk=choice_id)
    choice_form = ChoiceForm (request.POST or None, instance = a_choice)
    if choice_form.is_valid():
        choice = choice_form.save(commit=False)
        choice.question = get_object_or_404(Question, pk=question_id)
        choice.save()
        return redirect(reverse("polls:detail", kwargs={'pk':question_id,}))

    return render (request, "polls/edit_choice.html", {'choice_form': choice_form, 'choice_id':choice_id, 'question_id':question_id})

def delete_choice(request, question_id, choice_id):
    u = get_object_or_404(Choice, pk=choice_id)
    u.delete()
    return HttpResponseRedirect(reverse('polls:detail', kwargs={'pk':question_id}))
