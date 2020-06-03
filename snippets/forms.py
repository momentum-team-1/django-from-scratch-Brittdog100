from django import forms
from users.models import User
from .models import Snippet#, Tag

class SnippetForm(forms.ModelForm):
	class Meta:
		model = Snippet
		user = User
		fields = [
			'title',
			'lang',
			'code',
			'parent'
		]

# TODO: tag form