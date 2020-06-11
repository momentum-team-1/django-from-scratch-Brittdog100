from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Snippet
from .forms import SnippetForm

@login_required
def list_snippets(request):
	snippets = request.user.snippets.all()
	return render(request, "list.html", { "snippets": snippets })

@login_required
def add_snippet(request):
	if request.method == 'GET':
		form = SnippetForm()
	else:
		form = SnippetForm(data = request.POST)
		if form.is_valid():
			snip = form.save(commit = False)
			snip.author = request.user
			snip.save()
			snip.set_tags(form.cleaned_data['tag_names'])
			return redirect(to = 'list_snip')
	return render(request, "add_snip.html", { 'form': form })

def view_snippet(request, pk):
	snippet = get_object_or_404(Snippet, pk = pk)
	return render(request, "see_snip.html", { "snippet": snippet })

def edit_snippet(request, pk):
	snippet = get_object_or_404(Snippet, pk = pk)
	if request.method == 'GET':
		form = SnippetForm(instance = snippet)
	else:
		form = SnippetForm(data =  request.POST, instance = snippet)
		if form.is_valid():
			form.save()
			snippet.set_tags(form.cleaned_data['tag_names'])
			return redirect(to = 'list_snip')
	return render(request, "edit_snip.html", { "form": form, "snippet": snippet })

def make_child(request, parent_pk):
	parent = get_object_or_404(Snippet, pk = parent_pk)
	child = Snippet()
	child.author = request.user
	child.parent = parent
	child.code = parent.code
	child.lang = parent.lang
	child.title = ('Copy of "' + parent.title + '"')
	child.save()
	return edit_snippet(request, child.id)

def del_snip(request, pk):
	snippet = get_object_or_404(Snippet, pk = pk)
	if request.method == 'POST':
		snippet.delete()
		return redirect(to = 'list_snip')
	return render(request, 'del_snip.html', { "snippet": snippet })

def tag_view(request, tagname):
	pass #tag = get_object_or_404(Tag, tag = tagname)

@login_required
def search(request):
	query = request.GET.get('q')
	if query is not None:
		return render(request, "search.html", { "query": query, "user": request.user })
	else:
		return render(request, "search.html")

def homepage(request):
	return render(request, "home.html")
