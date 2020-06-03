from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Snippet
from .forms import SnippetForm

def list_snippets(request):
	snippets = request.user.snippets.all()
	return render(request, "list.html", {"snippets": snippets})

@login_required
def add_snippet(request):
	if request.method == 'GET':
		form = SnippetForm()
	else:
		form = SnippetForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect(to = 'list_snippets')
	return render(request, "add_snip.html", {'form': form})

def view_snippet(request, pk):
	snippet = get_object_or_404(Snippet, pk = pk)
	return render(request, "see_snip.html", {"snippet": snippet})

def edit_snippet(request, pk):
	snippet = get_object_or_404(Snippet, pk = pk)
	if request.method == 'GET':
		form = SnippetForm(instance = snippet)
	else:
		form = SnippetForm(data =  request.POST, instance = snippet)
		if form.is_valid():
			form.save()
			return redirect(to = 'list_snippets')
	return render(request, "edit_snip.html", {"form": form, "snippet": snippet})

def homepage(request):
	return render(request, "")
