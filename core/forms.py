from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
	model = Snippet
	user = User
	fields = [
		'lang',
		'title',
		'code'
	]