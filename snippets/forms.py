from django import forms
from users.models import User
from .models import Snippet#, Tag

class SnippetForm(forms.ModelForm):
	tag_names = forms.CharField(label = 'Tags', required = False, help_text = 'Enter a list of tags separated by commas.', widget = forms.TextInput())
	class Meta:
		model = Snippet
		author = User
		parent = Snippet
		fields = [
			'title',
			'lang',
			'code'
		]
