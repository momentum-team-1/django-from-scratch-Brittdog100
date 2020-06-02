from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm

def list_snippets(request):
	if request.method == 'GET':
		pass

def add_snippet(request):
	if request.method == 'GET':
		form = SnippetForm()
	else:
		form = SnippetForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect(to = 'list_snippets')
