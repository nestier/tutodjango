from polls.models import Question, Choice
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def check_size(value):
    if len(value) < 5 or len(value) > 30:
        raise ValidationError("Title shouldn't have less than 5 and more than 30 chars")

def without_asterix(value):
    if "*" in value:
        raise ValidationError("Value can't contain an asterix char")

def check_title(value):
    if len(value) < 4:
        raise ValidationError("El titulo debe contener mas de 4 caracteres")
    return value

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ('question_text', )

class ChoiceForm(forms.ModelForm):
    
    class Meta:
        model = Choice
        fields =('choice_text', 'votes', )
