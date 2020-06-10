from django.db import models
from users.models import User

class Snippet(models.Model):
	author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "snippets")
	title = models.CharField(max_length = 127)
	lang = models.CharField(max_length = 31)
	code = models.TextField(max_length = 32767)
	parent = models.ForeignKey(to = 'self', on_delete = models.SET_NULL, related_name = "children", null = True, blank = True)
	tags = models.ManyToManyField(to = 'Tag', related_name = "snips", blank = True)
	def get_tags(self):
		tl = [str(tag) for tag in self.tags.all()]
		return (", ".join(tl))
	def set_tags(self, tagstr):
		tl = [tag_name.strip() for tag_name in tagstr.split(",")]
		tout = []
		for tn in tl:
			tag = Tag.objects.filter(tag = tn).first()
			if tag is None:
				tag = Tag.objects.create(tag = tn)
			tout.append(tag)
		self.tags.set(tout)
	def __str__(self):
		return str('"' + self.title + '" in ' + self.lang + ' by ' + self.author)

class Tag(models.Model):
	tag = models.CharField(max_length = 15, unique = True, blank = True)
	def __str__(self):
		return self.tag
