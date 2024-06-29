from django.forms import ModelForm
from django import forms
from .models import Register, Feedback, MoodModel

class SignupForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        
class moodForm(ModelForm):
    class Meta:
        model = MoodModel
        fields = '__all__'