from django.views.generic import TemplateView

class Welcome(TemplateView):
	template_name = 'sistema/index.html'

class Profile(TemplateView):
    template_name = 'sistema/profile.html'
