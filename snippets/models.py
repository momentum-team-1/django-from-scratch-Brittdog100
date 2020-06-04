from django.db import models
from users.models import User

class Snippet(models.Model):
	author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "snippets")
	title = models.CharField(max_length = 127)
	lang = models.CharField(max_length = 31)
	code = models.TextField(max_length = 32767)
	parent = models.ForeignKey(to = 'self', on_delete = models.SET_NULL, related_name = "children", null = True, blank = True)
	#tags = models.ManyToManyField(to = 'Tag', related_name = "snips", null = True, blank = True)
	def __repr__():
		return str('"' + title + '" in ' + lang + ' by ' + author)

#class Tag(models.Model):
	#tag = models.CharField(max_length = 15, unique = True)
