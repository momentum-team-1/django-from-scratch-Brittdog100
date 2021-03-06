"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from snippets import views as snippet_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/', include('registration.backends.default.urls')),
	path('', snippet_views.homepage, name = 'home'),
	path('list/', snippet_views.list_snippets, name = "list_snip"),
	path('snippet/<int:pk>/edit/', snippet_views.edit_snippet, name = 'edit_snip'),
	path('snippet/add/', snippet_views.add_snippet, name = "add_snip"),
	path('snippet/<int:pk>/', snippet_views.view_snippet, name = "view_snip"),
	path('snippet/<int:parent_pk>/child', snippet_views.make_child, name = 'child_snip'),
	path('snippet/<int:pk>/del', snippet_views.del_snip, name = "del_snip"),
	path('search/', snippet_views.search, name = "search")
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),

		# For django versions before 2.0:
		# url(r'^__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns
